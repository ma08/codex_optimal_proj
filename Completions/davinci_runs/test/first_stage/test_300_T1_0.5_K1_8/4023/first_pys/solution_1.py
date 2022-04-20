

n = int(input())
a = list(map(int, input().split()))

# check if no empty spaces
if a[0] != a[-1]:
    print("NO")
    exit()

# check if all parts are the same height
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        print("NO")
        exit()

print("YES")