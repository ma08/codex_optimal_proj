

q = int(input())

for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) // n + int(sum(a) % n != 0))
