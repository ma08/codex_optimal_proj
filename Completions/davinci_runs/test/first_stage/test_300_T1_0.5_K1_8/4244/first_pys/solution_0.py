

N = int(input())
X = list(map(int, input().split()))

sum_x = sum(X)
sum_x_square = sum([x ** 2 for x in X])

ans = min([(sum_x_square - sum_x * p + N * p ** 2) for p in range(1, 101)])

print(ans)