import streamlit as st


def show_cost_comparison(naive_cost, optimal_cost):
    chart_data = {
        "Order": ["Naive", "Optimal"],
        "Cost": [naive_cost, optimal_cost]
    }

    st.bar_chart(
        chart_data,
        x="Order",
        y="Cost"
    )