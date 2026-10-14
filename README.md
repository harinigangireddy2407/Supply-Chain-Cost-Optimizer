
# 📦 Supply Chain Cost Optimizer

An interactive application that uses **Matrix Chain Multiplication (MCM) with Dynamic Programming** to find the minimum-cost multiplication order for sequential supply-chain transformation stages.

The application also supports **What-If Analysis and Scenario Comparison**, allowing users to evaluate different stage configurations and compare their computational costs.

## 📌 Problem Statement

In supply-chain and manufacturing processes, multiple transformation stages may need to be executed sequentially.

Although matrix multiplication is associative, different parenthesizations can require different numbers of scalar multiplications. Finding the optimal order reduces computational cost without changing the final result.

## 🎯 Objectives

- Model sequential supply-chain stages as matrices.
- Find the minimum-cost multiplication order using Dynamic Programming.
- Display the optimal parenthesization and DP cost table.
- Compare naive and optimized multiplication costs.
- Calculate cost savings and savings percentage.
- Evaluate and compare multiple supply-chain scenarios.

## ✨ Key Features

- Configure 2–10 transformation stages.
- Enter custom stage names and matrix dimensions.
- Validate matrix dimension compatibility.
- Optimize multiplication order using MCM.
- Display the optimal parenthesization.
- Visualize the Dynamic Programming cost table.
- Compare naive and optimal multiplication costs.
- Calculate cost savings and savings percentage.
- **What-If Analysis:** Save and evaluate different stage configurations.
- **Scenario Comparison:** Compare costs, savings, and optimal orders across saved scenarios.
- Compare each scenario's optimal cost against the first saved baseline.
- Visualize naive and optimal costs using a bar chart.
- Display algorithm time and space complexity.

## 🧠 Algorithm Approach

### 1. Naive Left-to-Right Multiplication

Calculates the scalar multiplication cost for one fixed multiplication order.

### 2. Matrix Chain Multiplication with Dynamic Programming

Evaluates different split positions and stores the minimum cost for each matrix-chain subproblem.

The recurrence is:

`m[i][j] = min(m[i][k] + m[k+1][j] + p[i-1] × p[k] × p[j])`

Here, `p` represents the matrix dimensions, and `k` represents a possible split position using the standard 1-based mathematical indexing.

The optimal parenthesization is reconstructed using the stored split positions.

## 📊 What-If Analysis and Scenario Comparison

Users can save multiple valid configurations and compare them to understand how changes in stage dimensions affect computational cost.

The comparison table displays:

- Number of stages
- Naive multiplication cost
- Optimal multiplication cost
- Cost saved and savings percentage
- Optimal parenthesization
- Change in optimal cost relative to the baseline

The first saved scenario acts as the baseline. A positive change indicates a higher cost, while a negative change indicates a lower cost.

Saved scenarios are maintained in Streamlit session state and are not permanently stored in a database.

## ⏱️ Complexity Analysis

Let `n` be the number of matrices.

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Naive Left-to-Right | O(n) | O(1) |
| MCM Dynamic Programming | O(n³) | O(n²) |

MCM evaluates all relevant subchains and split positions, resulting in O(n³) time and O(n²) space complexity.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Dynamic Programming
- Matrix Chain Multiplication

## 📁 Project Structure

```text
Supply-Chain-Cost-Optimizer/
├── app.py
├── backend/
│   ├── __init__.py
│   └── mcm.py
├── utils/
│   ├── __init__.py
│   └── charts.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### Prerequisites

- Python installed
- Git installed

### Installation

```bash
git clone https://github.com/harinigangireddy2407/Supply-Chain-Cost-Optimizer.git
cd Supply-Chain-Cost-Optimizer

python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies and run the application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Example

Consider the following matrix dimensions:

| Stage | Dimensions |
|---|---|
| Stage 1 | 40 × 20 |
| Stage 2 | 20 × 30 |
| Stage 3 | 30 × 10 |
| Stage 4 | 10 × 30 |

The expected results are:

- **Naive Cost:** 48,000
- **Optimal Cost:** 36,000
- **Cost Saved:** 12,000
- **Savings:** 25%

The application finds a lower-cost parenthesization using Dynamic Programming.

## 🔮 Future Enhancements

- Export scenario comparisons to CSV or PDF.
- Persist scenarios using a database.
- Support larger supply-chain configurations.
- Add visual explanations of the optimal multiplication order.

## 👩‍💻 Author

**Harini Gangireddy**

GitHub: [harinigangireddy2407](https://github.com/harinigangireddy2407)
