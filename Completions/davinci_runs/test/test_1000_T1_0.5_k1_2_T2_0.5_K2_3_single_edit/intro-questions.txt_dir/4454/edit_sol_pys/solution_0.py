

q = int(input())

for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print((sum(a) - 1) // n + 1)
