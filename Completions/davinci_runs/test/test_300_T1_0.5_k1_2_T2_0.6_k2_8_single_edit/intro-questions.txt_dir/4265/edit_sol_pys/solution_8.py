n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
b = [list(input()) for i in range(m)]


for i in range(n-m+1):
    for j in range(n-m+1):
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] != b[k][l]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            exit(0)

print("No")
