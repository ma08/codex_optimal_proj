

def main():
    ans1 = ""
    ans2 = ""
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    a = list(map(list,zip(*a)))
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i] = [1-a[i][k] for k in range(m)]
                break
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                a[i] = [1-a[i][k] for k in range(m)]
                break
    a = list(map(list,zip(*a)))
    if a == [[1]*m]*n:
        print("YES")
        print("".join(["0" for i in range(n)]))
        print("".join(["0" for i in range(m)]))
    else:
        print("NO")

if __name__ == "__main__":
    main()
