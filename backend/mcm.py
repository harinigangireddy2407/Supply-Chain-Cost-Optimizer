def matrix_chain_order(p):
    n = len(p) - 1

    # cost[i][j] = minimum cost to multiply Ai ... Aj
    cost = [[0] * n for _ in range(n)]

    # split[i][j] = position where the optimal split occurs
    split = [[0] * n for _ in range(n)]

    # length = number of matrices in the current chain
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            cost[i][j] = float("inf")

            for k in range(i, j):

                current_cost = (
                    cost[i][k]
                    + cost[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost
                    split[i][j] = k

    return cost, split

def get_parenthesization(split, i, j, names=None):
    if i == j:
        if names:
            return names[i]
        return f"A{i + 1}"

    k = split[i][j]

    left = get_parenthesization(split, i, k, names)
    right = get_parenthesization(split, k + 1, j, names)

    return f"({left} × {right})"

def naive_cost(p):
    """
    Calculates the cost of multiplying matrices strictly
    from left to right.

    Example:
    A1 × A2 × A3 × A4

    becomes:
    (((A1 × A2) × A3) × A4)
    """

    n = len(p) - 1

    if n <= 1:
        return 0

    total_cost = 0

    # Result of multiplying from the left initially has
    # the dimensions of A1.
    current_rows = p[0]
    current_columns = p[1]

    for i in range(2, n + 1):

        next_columns = p[i]

        # Cost of multiplying the current result with Ai
        total_cost += (
            current_rows
            * current_columns
            * next_columns
        )

        # The resulting matrix now has:
        # current_rows × next_columns
        current_columns = next_columns

    return total_cost
def get_cost_table(cost):
    n = len(cost)

    table = []

    for i in range(n):
        row = []

        for j in range(n):
            if j < i:
                row.append("-")
            else:
                row.append(cost[i][j])

        table.append(row)

    return table