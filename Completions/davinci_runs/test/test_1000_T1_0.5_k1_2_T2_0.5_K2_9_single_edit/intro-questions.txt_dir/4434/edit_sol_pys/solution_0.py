

# SOLUTION
# The problem can be solved with a greedy algorithm.
# The idea is to start from the center and move the figures to the closest cells
# If the center is not empty, we can move the figures in the center to the closest cells and then move the figures in the closest cells to the center
# We can repeat the process until all the figures are in the center
# Because we move the figures to the closest cells, the number of moves is minimized
# The time complexity is O(n^2), which is the size of the board

t = int(input())

for _ in range(t):
    n = int(input())
    print(n * (n // 2) ** 2)
