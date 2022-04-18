

# cook your dish here
    a, b, k = map(int, input().split())
t = int(input())
for _ in range(t):
    if k%2 == 0:
        print(k//2 * (a-b))
    else:
        print(k//2 * (a-b) + a)
