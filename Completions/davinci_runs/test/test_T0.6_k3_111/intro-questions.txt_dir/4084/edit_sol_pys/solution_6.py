

n, a, b = map(int, input().split())

# The pattern of the number of balls is:
# bbbrrrrrb, bbbrrrrrrrbbrrrrrb, bbbrrrrrrrrrbbrrrrrrrbbrrrrrrrb, and so on.
# The pattern is repeated after every (a + b) balls.
# The number of blue balls in the first (a + b) balls is (a + 1).
# The number of blue balls after the first (a + b) balls is equal to the number of blue balls in the first (a + b) balls
# The number of blue balls in the first n balls is equal to the number of blue balls in the first (a + b) balls multiplied by the number of repetitions of the pattern, plus the number of blue balls in the first n % (a + b) balls
print((a + 1) * (n // (a + b)) + (n % (a + b) + 1 if n % (a + b) <= a else a + 1))
