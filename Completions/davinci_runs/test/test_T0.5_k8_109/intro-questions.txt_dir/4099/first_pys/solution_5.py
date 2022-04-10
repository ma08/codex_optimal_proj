

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

# if the average score is m, then the sum of all scores should be m*n
# thus, we need to get (m*n - sum(a)) points on the final subject
final = m*n - sum(a)

if final > k:
    print(-1)
elif final < 0:
    print(0)
else:
    print(final)