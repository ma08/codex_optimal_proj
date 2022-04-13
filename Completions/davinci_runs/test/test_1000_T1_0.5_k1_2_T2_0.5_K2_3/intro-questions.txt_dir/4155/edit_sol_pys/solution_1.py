# ABC081B

n = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        if a[i] % 2 != 0:
            print(ans)
            exit()
    for i in range(n):
        a[i] //= 2
    ans += 1

print(ans)
