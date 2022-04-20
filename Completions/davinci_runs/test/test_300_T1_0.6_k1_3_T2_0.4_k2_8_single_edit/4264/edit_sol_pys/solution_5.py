n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


for i in range(q):
    ans = "no"
    for j in range(n):
        for k in range(n):
            if a[j] + a[k] == m[i]:
                ans = "yes"
                break
        if ans == "yes":
            break
    print(ans)
