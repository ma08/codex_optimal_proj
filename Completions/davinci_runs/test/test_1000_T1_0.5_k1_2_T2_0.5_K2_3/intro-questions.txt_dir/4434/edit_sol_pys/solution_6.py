

# solution
# the problem can be solved with a greedy algorithm.
# the idea is to start from the center and move the figures to the closest cells.
# if the center is not empty, we can move the figures in the center to the closest empty cells
# and then move the figures in the closest empty cells to the center.
# we can repeat the process until all the figures are in the center.
# because we move the figures to the closest cells, the number of moves is minimized.
# the time complexity is O(n^2), which is the size of the board.

T = int(input())

for _ in range(T):
    n = int(input())
    print(n * (n // 2) ** 2)
