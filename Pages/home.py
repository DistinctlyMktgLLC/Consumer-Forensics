import streamlit as st

def show_home():
    st.title("Neighborhood Insights Dashboard - Overview")
    st.header("Executive Summary")
    st.write("""
    This dashboard provides key insights into neighborhood demographics, survey results, and business data, highlighting potential investment opportunities. 
    The data visualized here represents a comprehensive survey of individuals across various US neighborhoods.

    ## Understanding Negative Worth in Financial Patterns
    Why might someone's worth appear negative? It's a curious phenomenon that often arises from the complex interplay between real spending habits and cognitive biases. Think of it as a peek into the hidden intricacies of financial behaviors that traditional metrics often overlook.

    Negative worth in our visualization reflects how spending patterns manifest in ways that might not be immediately obvious. For example, consider how expenses, debts, and financial obligations accumulate over time, often influenced by various cognitive biases. People might overspend due to optimism bias, believing they will earn more in the future to cover their current expenses. Or they might fall prey to the bandwagon effect, making purchases because "everyone else is doing it."

    These spending behaviors can lead to financial outcomes that are starkly different from what one might expect. When tax season comes around, the real financial picture emerges, often revealing deficits that weren't accounted for during the year. Thus, a negative worth in our data serves as a poignant reminder of how our psychological tendencies can shape, and sometimes distort, our financial realities.

    ## Key Findings:
    1. Diverse Segment Distribution: Our survey captures a wide range of distinct segments, offering a comprehensive view of consumer preferences and behaviors.
    2. Geographical Spread: The interactive map showcases the nationwide distribution of our survey respondents, allowing for region-specific insights.
    3. Demographic Variety: We have a diverse range of respondents across different income levels, and backgrounds.

    **Note:** This represents only a portion of the available data. For full access, contact [darnel.m@distinctlymktg.com](mailto:darnel.m@distinctlymktg.com).
    """)
    st.markdown("Dashboard powered by Distinct.ly. Data last updated: July 30 2024 11:05 pm EST")
