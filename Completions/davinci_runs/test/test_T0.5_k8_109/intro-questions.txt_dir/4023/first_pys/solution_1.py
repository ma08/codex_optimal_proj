

n = int(input())
a = [int(x) for x in input().split()]

# first part: check if there are any gaps
for i in range(1, n):
    if a[i - 1] != a[i]:
        print("NO")
        exit()

print("YES")