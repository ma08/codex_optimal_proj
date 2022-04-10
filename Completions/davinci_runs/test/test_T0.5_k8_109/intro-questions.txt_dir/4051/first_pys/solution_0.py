


n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    if a[i] == a[i-1] + 1:
        print("NO")
        exit()

print("YES")