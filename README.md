# 📦 Supply Chain Cost Optimizer

An interactive application that uses **Matrix Chain Multiplication (MCM) with Dynamic Programming** to determine the minimum-cost order for performing a sequence of matrix-based transformation stages.

The project models a manufacturing/supply-chain process where a product passes through multiple sequential stages. Each stage is represented as a matrix, and the application finds the most cost-efficient way to combine these stages.

---

## 📌 Problem Statement

In a supply chain or manufacturing process, multiple transformation stages may need to be performed sequentially.

Although matrix multiplication is associative, different multiplication orders can require different numbers of scalar multiplications.

For example:
(A1 × A2) × A3 and A1 × (A2 × A3) produce the same final result, but their computational costs may be different.

---

## 🎯 Objectives

- Model sequential supply-chain transformation stages as a matrix chain.
- Determine the minimum-cost multiplication order using Matrix Chain Multiplication.
- Recover and display the optimal parenthesization.
- Compare the optimized cost with a fixed left-to-right multiplication order.
- Calculate the total cost saved and savings percentage.

---

## ✨ Key Features

- Enter the number of transformation stages.
- Provide custom names for each stage.
- Define matrix dimensions for every stage.
- Validate matrix dimension compatibility.
- Find the optimal multiplication order using Dynamic Programming.
- Display the optimal parenthesization.
- Display the Dynamic Programming cost table.
- Compare naive and optimized multiplication costs.
- Calculate cost savings and savings percentage.
- Visualize the cost comparison using a bar chart.
- Display time and space complexity of the approaches.

---

## 🧠 Approach

The project compares two approaches:

- **Naive Left-to-Right:** Calculates the cost of multiplying the matrices in one fixed order.
- **Matrix Chain Multiplication:** Uses Dynamic Programming to evaluate different multiplication orders and find the one with minimum cost.

The optimal parenthesization is recovered using the split positions stored during the Dynamic Programming process.

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|---|---:|---:|
| Naive Left-to-Right | O(n) | O(1) |
| MCM Dynamic Programming | O(n³) | O(n²) |

The naive approach calculates only one fixed order, while MCM searches for the minimum-cost order.

## 🏗️ Project Structure

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


### 6. Technologies
```markdown
## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Dynamic Programming
- Matrix Chain Multiplication

## 🚀 How to Run

```bash
git clone https://github.com/harinigangireddy2407/Supply-Chain-Cost-Optimizer.git
cd Supply-Chain-Cost-Optimizer
pip install -r requirements.txt
streamlit run app.py


### 8. Example
```markdown
## 🧪 Example

For the following matrix chain:

| Stage | Dimension |
|---|---|
| Stage 1 | 40 × 20 |
| Stage 2 | 20 × 30 |
| Stage 3 | 30 × 10 |
| Stage 4 | 10 × 30 |

The application produces:

- **Naive Cost:** 48,000
- **Optimal Cost:** 26,000
- **Cost Saved:** 22,000
- **Savings:** 45.83%