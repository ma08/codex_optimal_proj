

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(n)]
    a = list(map(list,zip(*a))) # 列転置
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i] = [1-b for b in a[i]]
                break
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                a[i] = [1-b for b in a[i]]
                break
    a = list(map(list,zip(*a))) # 行転置
    if a == [[1]*m]*n:
        print("YES")
        print("".join(["0"]*n))
        print("".join(["0"]*m))
    else:
        print("NO")

if __name__ == "__main__":
    main()
