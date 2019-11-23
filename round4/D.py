#!/usr/bin/env python
"""https://cses.fi/320/task/D
Uolevi wants to buy a plot of land from a nearby forest. The plot must be square-shaped and there has to be exactly x trees on the plot.

How many ways are there to choose a plot?

Input

On the first line there are three integers n, m and x: the height and width of the forest and the required amount of trees.

n lines follow, describing the forest. On each line there are m characters. Character . means empty space and * means a tree.

Output

Output a single integer: the number of ways to choose a plot.

Constraints
1≤n,m≤2000
0≤x≤n⋅m
Examples

Input:
4 6 3
..**..
**....
*...*.
..*...

Output:
3
"""


def get_flat_index(i, j, cols):
    return i * cols + j


def get_sum(row, col, side, prefix_sum_array):
    # Check if sum from [row, col] to [row + side, col + side] == trees
    end_row = row + side - 1
    end_col = col + side - 1
    # print(f"Ends at {end_row} {end_col}")
    s_A_i = get_flat_index(end_row, end_col, cols)
    # print(f"s_A_i: {s_A_i}")
    s_A = prefix_sum_array[s_A_i]
    if col - 1 < 0:
        s_B = 0
    else:
        s_B_i = get_flat_index(end_row, col - 1, cols)
        s_B = prefix_sum_array[s_B_i]
    if row - 1 < 0:
        s_C = 0
    else:
        s_C_i = get_flat_index(row - 1, end_col, cols)
        s_C = prefix_sum_array[s_C_i]
    if (col - 1 < 0) or (row - 1 < 0):
        s_D = 0
    else:
        s_D_i = get_flat_index(row - 1, col - 1, cols)
        s_D = prefix_sum_array[s_D_i]
    s = s_A - s_B - s_C + s_D
    return s


def num_ways(forest, trees, rows, cols):
    prefix_sum_array = [0] * cols * rows
    i = -1
    ways = 0
    for row_i, row in enumerate(forest):
        curr_sum = 0
        # print(row)
        for col_i, c in enumerate(row):
            i += 1
            if c == '*':
                curr_sum += 1  # It's a tree!
            if row_i > 0:
                above_idx = get_flat_index(row_i - 1, col_i, cols)
                prefix_sum_array[i] = curr_sum + prefix_sum_array[above_idx]
            else:
                prefix_sum_array[i] = curr_sum
    # print(prefix_sum_array)
    # print(f"Checking side {side}")
    for row in range(rows):
        for col in range(cols):
            # Binary search over square's sides
            # print(f"Checking row {row} and col {col} for sides [{l}, {r})")
            # First binary serch
            first_i = 0
            l, r = 1, min(rows - row, cols - col) + 1
            while l < r:
                side = (l + r) // 2
                s = get_sum(row, col, side, prefix_sum_array)
                # print(f"s_A: {s_A} {s_B} {s_C} {s_D}")
                # print(f"SUM: {s}")
                if s < trees - 1:
                    l = side + 1
                elif s > trees - 1:
                    r = side
                elif s == trees - 1:
                    if side + 1 >= l or get_sum(row, col, side + 1,
                                                prefix_sum_array) > trees - 1:
                        first_i = side
                        break
                    # print(f"l {l} r {r} side {side} s {s}")
                    l = side + 1  # Check next size up
            # second binary serch
            second_i = 0
            l, r = 1, min(rows - row, cols - col) + 1
            while l < r:
                side = (l + r) // 2
                s = get_sum(row, col, side, prefix_sum_array)
                # print(f"s_A: {s_A} {s_B} {s_C} {s_D}")
                # print(f"SUM: {s}")
                if s < trees:
                    l = side + 1
                elif s > trees:
                    r = side
                elif s == trees:
                    if side + 1 >= l or get_sum(row, col, side + 1,
                                                prefix_sum_array) > trees:
                        second_i = side
                        break
                    # print(f"l {l} r {r} side {side} s {s}")
                    l = side + 1  # Check next size up
        ways += max(0, second_i - first_i)
    return ways


if __name__ == "__main__":
    rows, cols, trees = [int(x) for x in input().split()]
    forest = []
    for _ in range(rows):
        row = input()
        forest.append(row)
    print(num_ways(forest, trees, rows, cols))
