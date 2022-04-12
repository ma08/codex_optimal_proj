
# this is a test
q = int(input())

for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) // n + (sum(a) % n > 0))
