# Project Report: Cost Structure and Channel-Wise Profitability Analysis for Multi-Channel Restaurants

## Abstract
This project demonstrates how a restaurant operator can compare revenue, modeled operating costs, profit and profit margin across dine-in, online delivery, takeaway and aggregator delivery. Python, pandas, Plotly and Streamlit are used to prepare the dataset and provide an interactive dashboard. The included dataset is synthetic and is intended for demonstration, not as evidence about any real restaurant.

## 1. Problem Statement
Restaurants selling through several channels may face different labor, packaging, discount and platform-fee structures. Revenue alone can be misleading if the cost to serve a channel is high. The project creates a repeatable analytical view of channel-level contribution.

## 2. Objectives
- Compare revenue, costs, profit and profit margin across sales channels.
- Quantify modeled food, labor, packaging, platform-fee, overhead and discount costs.
- Explore monthly performance and regional differences.
- Provide practical recommendations and an interactive dashboard.

## 3. Tools
Python 3, pandas, NumPy, Plotly and Streamlit. Input data is stored in CSV format.

## 4. Dataset and Method
The demonstration dataset contains 900 synthetic order-summary records dated in 2025. Fields include order date, region, cuisine type, sales channel, order count, revenue and six cost categories. Costs are generated using plausible illustrative percentages. Profit = Revenue - Total Cost. Profit Margin (%) = Profit / Revenue × 100. These assumptions are artificial and must be replaced with verified point-of-sale and accounting data for real decisions.

## 5. Workflow
1. Load and inspect the CSV.
2. Check data types and ensure numeric fields are available.
3. Aggregate revenue, costs and profit by sales channel.
4. Calculate channel margin and summarize cost categories.
5. Analyze monthly revenue and profit trends.
6. Present filters, charts, tables and observations in Streamlit.
7. Translate results into recommendations while documenting limitations.

## 6. Dashboard Features
- KPI cards for total revenue, costs, modeled profit and margin.
- Channel-wise revenue and profit charts.
- Cost-structure pie chart.
- Monthly trend chart.
- Channel comparison table and automatic observations.
- Region and channel filters; CSV export.

## 7. Key Questions Answered
Which channel contributes the most modeled profit? Which has the highest margin? Which cost category accounts for the largest total? Do revenue and profit move together over time? The dashboard calculates answers dynamically based on the selected filters.

## 8. Recommendations
- Evaluate aggregator fees and discounts using contribution margin rather than sales alone.
- Review packaging standards and delivery-specific menu pricing.
- Match staffing to demand by time and channel.
- Monitor food-cost variance and wastage.
- Run controlled promotions and measure incremental profit.
- Validate assumptions against actual invoices, payroll, platform statements and POS data.

## 9. Limitations
The dataset is synthetic, costs are generated from assumptions, and records are not audited transactions. Taxes, refunds, rent allocation, inventory waste and working-capital effects may not be fully represented. Results should not be presented as actual performance of a named restaurant.

## 10. Conclusion
The project illustrates a practical analytics workflow for comparing channel-level economics. A dashboard makes cost drivers visible and supports better questions for managers. Real operational decisions require validated data, consistent cost allocation and regular review.
