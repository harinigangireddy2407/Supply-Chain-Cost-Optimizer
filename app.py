import streamlit as st
import pandas as pd
from backend.mcm import (
    matrix_chain_order,
    get_parenthesization,
    naive_cost,
    get_cost_table
)
from utils.charts import show_cost_comparison


st.set_page_config(
    page_title="Supply Chain Cost Optimizer",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Supply Chain Cost Optimizer")
st.write(
    "Optimize the order of sequential transformation stages "
    "using Matrix Chain Multiplication and Dynamic Programming."
)

st.header("Define Supply Chain Stages")

num_stages = st.number_input(
    "Number of stages",
    min_value=2,
    max_value=10,
    value=4,
    step=1
)

dimensions = []
stage_names = []

st.subheader("Enter Stage Details")

for i in range(num_stages):
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        stage_name = st.text_input(
            f"Stage {i + 1}",
            value=f"Stage {i + 1}",
            key=f"name_{i}"
        )

    with col2:
        rows = st.number_input(
            f"Rows {i + 1}",
            min_value=1,
            value=10,
            key=f"rows_{i}"
        )

    with col3:
        cols = st.number_input(
            f"Columns {i + 1}",
            min_value=1,
            value=20,
            key=f"cols_{i}"
        )

    stage_names.append(stage_name)
    dimensions.append((rows, cols))


if st.button("🚀 Optimize Supply Chain", type="primary"):

    valid_dimensions = True
    valid_names = True

    for name in stage_names:
        if not name.strip():
            valid_names = False
            break

    for i in range(len(dimensions) - 1):
        if dimensions[i][1] != dimensions[i + 1][0]:
            valid_dimensions = False
            break

    if not valid_names:
        st.error("Please enter a name for every supply chain stage.")

    elif not valid_dimensions:
        st.error(
            "Invalid matrix dimensions! "
            "The columns of each stage must match the rows of the next stage."
        )

    
    else:
        p = [dimensions[0][0]]

        for rows, cols in dimensions:
            p.append(cols)

        cost, split = matrix_chain_order(p)

        optimal_cost = cost[0][num_stages - 1]
        dp_table = get_cost_table(cost)
        optimal_order = get_parenthesization(
            split,
            0,
            num_stages - 1,
            stage_names
        )

        naive = naive_cost(p)

        st.success("Optimization completed!")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Optimal Cost", f"{optimal_cost:,}")

        with col2:
            st.metric("Naive Cost", f"{naive:,}")

        with col3:
            savings = naive - optimal_cost
            st.metric("Cost Saved", f"{savings:,}")

        with col4:
            if naive > 0:
               savings_percentage = (savings / naive) * 100
            else:
               savings_percentage = 0

            st.metric(
                "Savings %",
                f"{savings_percentage:.2f}%"
            )

        st.subheader("Optimal Parenthesization")

        st.code(optimal_order)

        st.subheader("Dynamic Programming Cost Table")

        labels = stage_names

        dp_dataframe = pd.DataFrame(
            dp_table,
            index=labels,
            columns=labels
        )

        st.dataframe(
            dp_dataframe,
            use_container_width=True
        )

        st.subheader("Cost Comparison")

        show_cost_comparison(naive, optimal_cost)

        

        st.subheader("Algorithm Complexity")

complexity_data = {
    "Approach": [
        "Naive Left-to-Right",
        "MCM Dynamic Programming"
    ],
    "Purpose": [
        "Calculates cost for one fixed order",
        "Finds the minimum-cost order"
    ],
    "Time Complexity": [
        "O(n)",
        "O(n³)"
    ],
    "Space Complexity": [
        "O(1)",
        "O(n²)"
    ]
}

st.table(complexity_data)

st.write(
    "The naive approach calculates the cost of one predetermined "
    "left-to-right multiplication order. MCM uses Dynamic Programming "
    "to evaluate different split positions and find the order with "
    "minimum multiplication cost."
)