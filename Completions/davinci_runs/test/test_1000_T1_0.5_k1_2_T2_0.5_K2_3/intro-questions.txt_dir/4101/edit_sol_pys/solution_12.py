

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    a = list(map(list,zip(*a)))
    for i in range(n+m):
        if i < n:
            for j in range(m):
                if a[i][j] == 1:
                    a[i] = [1-a for a in a[i]]
                    break
        else:
            for j in range(n):
                if a[i-n][j] == 1:
                    a[i-n] = [1-a for a in a[i-n]]
                    break
    # a = list(map(list,zip(*a)))
    if a == [[1]*m]*n:
        print("YES")
        print("".join(["0" for _ in range(n)]))
        print("".join(["0" for _ in range(m)]))
    else:
        print("NO")

if __name__ == "__main__":
    main()
