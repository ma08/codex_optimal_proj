

n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a)

if a_sorted[0] == a_sorted[1]:
    print("YES")
else:
    print("NO")
