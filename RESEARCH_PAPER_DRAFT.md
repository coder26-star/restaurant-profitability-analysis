# Channel-Wise Cost Structure and Profitability in Multi-Channel Restaurants: A Demonstration Analytics Framework

**Document type:** Student project research-paper draft  
**Author:** [Add student name before publication]  
**Important note:** This is a project paper draft, not an approved or published research paper. The underlying data is synthetic.

## Abstract
Multi-channel restaurants may receive orders through dine-in, takeaway, direct online delivery and third-party aggregators. Each channel can produce different revenue and cost patterns. This project presents a reproducible descriptive-analytics framework that calculates channel-level revenue, modeled cost, profit and profit margin, and visualizes monthly performance. A synthetic dataset of 900 records is analyzed using Python, pandas, Plotly and Streamlit. The framework demonstrates how cost decomposition can help managers identify questions about platform fees, packaging, discounts and staffing. Because the dataset is simulated, no claims are made about actual restaurants. Future work should apply the framework to audited transaction data and include taxes, refunds, rent allocation and uncertainty analysis.

## Keywords
Restaurant analytics; channel profitability; cost structure; Python; business intelligence; Streamlit.

## 1. Introduction
Restaurant operators increasingly use several sales channels. Channel-level sales totals do not by themselves reveal the cost of fulfilling orders. A high-revenue channel may have a lower contribution after commissions, discounts, packaging and labor. This project demonstrates a simple analytics workflow that separates revenue and modeled costs to make comparisons transparent.

## 2. Research Questions
1. How can revenue, modeled cost and profit be summarized by sales channel?
2. Which modeled cost categories account for the largest total amounts?
3. How can a dashboard help stakeholders inspect monthly and channel-level patterns?

## 3. Methodology
A synthetic dataset was generated with 900 order-summary records across four sales channels, four regions and five cuisine categories. Revenue and cost categories are numerical demonstration values. Total cost is the sum of food, labor, packaging, platform fee, overhead and discounts. Profit is revenue minus total cost; margin is profit divided by revenue multiplied by 100. Group-by aggregation and interactive visualizations are implemented in Python.

## 4. Results Presentation
The accompanying dashboard calculates results from the included CSV and updates when channel or region filters change. It displays KPI cards, channel-level revenue and profit, a cost composition chart, monthly trends and a comparison table. Exact values should be read from the dashboard because they are generated from the bundled dataset and selected filters; they should not be generalized to real restaurants.

## 5. Discussion
The framework encourages decision-makers to distinguish sales volume from channel contribution. Platform fees and discounts deserve attention where applicable, while labor and packaging should be allocated consistently. The most important methodological requirement is to avoid treating synthetic assumptions as measured facts.

## 6. Limitations and Ethics
The dataset is synthetic and contains no personal data. The model does not establish causality and may omit important costs such as refunds, taxes, rent, waste and payment processing. The dashboard is educational and is not a substitute for accounting review.

## 7. Conclusion
A compact Python dashboard can make channel economics easier to inspect and discuss. Applying the framework to real data requires data-quality checks, documented allocation rules and validation with finance and operations teams.

## References
This draft uses standard descriptive-analytics methods and does not claim a literature review or peer-reviewed publication. Before submitting as a formal research paper, add verified academic sources from a library database and follow the institution's citation requirements.
