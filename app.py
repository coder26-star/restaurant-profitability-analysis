import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Restaurant Profitability Analytics", page_icon="🍽️", layout="wide")
st.title("🍽️ Cost Structure & Channel-Wise Profitability")
st.caption("Exploratory business analytics dashboard | Currency: INR | Dataset is synthetic and created for demonstration.")
file = Path(__file__).parent / "restaurant_sales_costs.csv"
df = pd.read_csv(file, parse_dates=["Order_Date"])
channels = st.sidebar.multiselect("Sales channel", sorted(df.Sales_Channel.unique()), default=sorted(df.Sales_Channel.unique()))
regions = st.sidebar.multiselect("Region", sorted(df.Region.unique()), default=sorted(df.Region.unique()))
d = df[df.Sales_Channel.isin(channels) & df.Region.isin(regions)].copy()
if d.empty:
    st.warning("Select at least one channel and one region.")
    st.stop()
revenue = d.Revenue_INR.sum()
cost = d.Total_Cost_INR.sum()
profit = d.Profit_INR.sum()
margin = profit / revenue * 100 if revenue else 0
c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{revenue:,.0f}")
c2.metric("Total Costs", f"₹{cost:,.0f}")
c3.metric("Operating Profit*", f"₹{profit:,.0f}")
c4.metric("Profit Margin", f"{margin:.1f}%")
st.caption("*Profit here means revenue less the modeled costs in this dataset; it is not audited accounting profit.")
a,b = st.columns(2)
channel = d.groupby("Sales_Channel", as_index=False).agg(Revenue=("Revenue_INR","sum"), Profit=("Profit_INR","sum"), Orders=("Orders","sum"))
channel["Profit_Margin_Pct"] = channel.Profit / channel.Revenue * 100
a.plotly_chart(px.bar(channel, x="Sales_Channel", y="Revenue", title="Revenue by Sales Channel", color="Sales_Channel"), use_container_width=True)
b.plotly_chart(px.bar(channel, x="Sales_Channel", y="Profit", title="Profit by Sales Channel", color="Sales_Channel"), use_container_width=True)
cost_cols = ["Food_Cost_INR","Labor_Cost_INR","Packaging_Cost_INR","Platform_Fee_INR","Overhead_INR","Discounts_INR"]
costs = d[cost_cols].sum().rename_axis("Cost_Category").reset_index(name="Amount_INR")
costs["Cost_Category"] = costs["Cost_Category"].str.replace("_INR","",regex=False).str.replace("_"," ")
a,b = st.columns(2)
a.plotly_chart(px.pie(costs, names="Cost_Category", values="Amount_INR", title="Cost Structure Breakdown"), use_container_width=True)
monthly = d.assign(Month=d.Order_Date.dt.to_period("M").astype(str)).groupby("Month",as_index=False).agg(Revenue=("Revenue_INR","sum"),Profit=("Profit_INR","sum"))
b.plotly_chart(px.line(monthly, x="Month", y=["Revenue","Profit"], markers=True, title="Monthly Revenue and Profit Trend"), use_container_width=True)
st.subheader("Channel comparison")
st.dataframe(channel.sort_values("Profit", ascending=False).style.format({"Revenue":"₹{:,.0f}","Profit":"₹{:,.0f}","Profit_Margin_Pct":"{:.1f}%"}), use_container_width=True)
st.subheader("Automated observations")
best = channel.sort_values("Profit_Margin_Pct", ascending=False).iloc[0]
worst = channel.sort_values("Profit_Margin_Pct").iloc[0]
largest_cost = costs.sort_values("Amount_INR", ascending=False).iloc[0]
st.write(f"- Highest modeled profit margin in the selected data: **{best.Sales_Channel} ({best.Profit_Margin_Pct:.1f}%)**.")
st.write(f"- Lowest modeled profit margin in the selected data: **{worst.Sales_Channel} ({worst.Profit_Margin_Pct:.1f}%)**.")
st.write(f"- Largest cost category: **{largest_cost.Cost_Category} (₹{largest_cost.Amount_INR:,.0f})**.")
st.info("Recommendations: review aggregator commission and discount leakage; compare contribution margin by channel; optimize staffing and packaging; validate assumptions against actual point-of-sale and accounting records before business decisions.")
with st.expander("Dataset preview"):
    st.dataframe(d.head(100), use_container_width=True)
st.download_button("Download filtered data as CSV", d.to_csv(index=False).encode("utf-8"), "restaurant_filtered_data.csv", "text/csv")
