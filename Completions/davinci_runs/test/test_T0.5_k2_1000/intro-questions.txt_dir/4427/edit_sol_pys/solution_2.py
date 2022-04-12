
# AtCoder Beginner Contest 079
# C - Train Ticket
# Solve

# input
r, D, x2000 = map(int, input().split())

# output
for i in range(10):
    x2000 = r * x2000 - D
    print(x2000)
