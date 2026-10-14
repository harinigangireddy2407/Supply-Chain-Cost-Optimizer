
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

if "scenarios" not in st.session_state:
    st.session_state.scenarios = []

st.title("📦 Supply Chain Cost Optimizer")
st.write(
    "Optimize supply chain transformation stages using "
    "Matrix Chain Multiplication and Dynamic Programming."
)

st.header("Define Supply Chain Stages")

num_stages = st.number_input(
    "Number of stages",
    min_value=2,
    max_value=10,
    value=4,
    step=1
)

scenario_name = st.text_input(
    "Scenario name",
    value=f"Scenario {len(st.session_state.scenarios) + 1}",
    help="Give each configuration a name, such as Baseline or Improved Plan."
)

dimensions = []
stage_names = []

st.subheader("Enter Stage Details")

default_columns = [20, 30, 40, 30, 20, 30, 40, 20, 30, 10]

for i in range(int(num_stages)):
    col1, col2, col3 = st.columns([2, 1, 1])

    default_rows = (
        10 if i == 0
        else st.session_state.get(f"cols_{i - 1}", default_columns[i - 1])
    )

    with col1:
        name = st.text_input(
            f"Stage {i + 1} name",
            value=f"Stage {i + 1}",
            key=f"name_{i}"
        )

    with col2:
        rows = st.number_input(
            f"Rows {i + 1}",
            min_value=1,
            value=int(default_rows),
            key=f"rows_{i}"
        )

    with col3:
        cols = st.number_input(
            f"Columns {i + 1}",
            min_value=1,
            value=default_columns[i],
            key=f"cols_{i}"
        )

    stage_names.append(name)
    dimensions.append((int(rows), int(cols)))


if st.button("🚀 Optimize and Save Scenario", type="primary"):

    valid_names = all(name.strip() for name in stage_names)

    valid_dimensions = all(
        dimensions[i][1] == dimensions[i + 1][0]
        for i in range(len(dimensions) - 1)
    )

    if not scenario_name.strip():
        st.error("Please enter a scenario name.")

    elif not valid_names:
        st.error("Please enter a name for every stage.")

    elif not valid_dimensions:
        st.error(
            "Invalid dimensions! The columns of each stage must "
            "match the rows of the next stage."
        )

    else:
        p = [dimensions[0][0]]
        for rows, cols in dimensions:
            p.append(cols)

        cost, split = matrix_chain_order(p)

        optimal = cost[0][int(num_stages) - 1]
        naive = naive_cost(p)
        savings = naive - optimal
        savings_percentage = (savings / naive * 100) if naive else 0

        optimal_order = get_parenthesization(
            split, 0, int(num_stages) - 1, stage_names
        )

        scenario = {
            "Scenario": scenario_name.strip(),
            "Stages": int(num_stages),
            "Naive Cost": naive,
            "Optimal Cost": optimal,
            "Cost Saved": savings,
            "Savings (%)": round(savings_percentage, 2),
            "Optimal Order": optimal_order,
            "Dimensions": dimensions.copy()
        }

        # Save this configuration for comparison.
        st.session_state.scenarios.append(scenario)

        st.session_state.latest_result = {
            **scenario,
            "Cost Table": get_cost_table(cost),
            "Stage Names": stage_names.copy()
        }

        st.success(f"'{scenario_name}' optimized and saved successfully!")


# Display the most recently optimized scenario.
if "latest_result" in st.session_state:
    result = st.session_state.latest_result

    st.header(f"Results: {result['Scenario']}")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Optimal Cost", f"{result['Optimal Cost']:,}")
    c2.metric("Naive Cost", f"{result['Naive Cost']:,}")
    c3.metric("Cost Saved", f"{result['Cost Saved']:,}")
    c4.metric("Savings", f"{result['Savings (%)']:.2f}%")

    st.subheader("Optimal Parenthesization")
    st.code(result["Optimal Order"])

    st.subheader("Dynamic Programming Cost Table")

    dp_dataframe = pd.DataFrame(
        result["Cost Table"],
        index=result["Stage Names"],
        columns=result["Stage Names"]
    )

    st.dataframe(dp_dataframe, use_container_width=True)

    st.subheader("Cost Comparison")
    show_cost_comparison(
        result["Naive Cost"],
        result["Optimal Cost"]
    )


# Compare every saved scenario.
st.header("What-If Analysis: Scenario Comparison")

if st.session_state.scenarios:
    comparison_df = pd.DataFrame([
        {
            "Scenario": s["Scenario"],
            "Stages": s["Stages"],
            "Naive Cost": s["Naive Cost"],
            "Optimal Cost": s["Optimal Cost"],
            "Cost Saved": s["Cost Saved"],
            "Savings (%)": s["Savings (%)"],
            "Optimal Order": s["Optimal Order"]
        }
        for s in st.session_state.scenarios
    ])

    baseline_cost = st.session_state.scenarios[0]["Optimal Cost"]

    comparison_df["Change vs Baseline"] = (
        comparison_df["Optimal Cost"] - baseline_cost
    )

    st.caption(
        "The first saved scenario is the baseline. "
        "A negative change means a lower cost than the baseline."
    )

    st.dataframe(comparison_df, use_container_width=True)

    st.subheader("Optimal Cost Across Scenarios")

    chart_df = comparison_df.set_index("Scenario")[
        ["Naive Cost", "Optimal Cost"]
    ]

    st.bar_chart(chart_df, stack=False)
    
    best_scenario = min(
        st.session_state.scenarios,
        key=lambda s: s["Optimal Cost"]
    )

    st.success(
        f"Lowest-cost scenario: {best_scenario['Scenario']} "
        f"with an optimal cost of {best_scenario['Optimal Cost']:,}."
    )

    if st.button("Clear All Saved Scenarios"):
        st.session_state.scenarios = []
        st.session_state.pop("latest_result", None)
        st.rerun()

else:
    st.info(
        "Optimize and save at least one scenario. "
        "Then change the stage dimensions and save another scenario "
        "to compare different supply chain plans."
    )


st.header("Algorithm Complexity")

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
    "left-to-right multiplication order. Matrix Chain Multiplication "
    "uses Dynamic Programming to evaluate different split positions "
    "and find the order with minimum multiplication cost."
)
