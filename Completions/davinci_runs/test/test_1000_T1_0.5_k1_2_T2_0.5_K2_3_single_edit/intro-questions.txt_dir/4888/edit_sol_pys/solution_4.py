

n, T = map(int, input().split())
tasks = list(map(int, input().split()))

t = 0
i = 1
while t < T and i <= n:
    t += tasks[i-1]
    i += 1 

print(i)
