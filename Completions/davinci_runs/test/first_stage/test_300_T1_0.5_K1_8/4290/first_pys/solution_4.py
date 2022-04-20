


# n: number of even balls
# m: number of odd balls
n, m = map(int, input().split())

# the answer is the number of ways to choose 2 balls from n+m
# balls, which is the same as the number of ways to choose 2
# balls from m+n-2 balls, since we can only choose odd balls
# from the m+n-2 balls
print(n*m)