

# SOLUTION
# The problem can be solved with a greedy algorithm.
# The idea is to start from the center and move the figures to the adjacent cells.
# If the center is not empty, we can move the figures in the center to the adjacent cells
# and then move the figures in the adjacent cells to the center.
# We can repeat the process until all the figures are in the adjacent cells.
# Because we move the figures to the adjacent cells, the number of moves is minimized.
# The time complexity is O(n), which is the size of the board.

t = int(input())

for _ in range(t):
    n = int(input())
    print(n * (n // 2) ** 2)
