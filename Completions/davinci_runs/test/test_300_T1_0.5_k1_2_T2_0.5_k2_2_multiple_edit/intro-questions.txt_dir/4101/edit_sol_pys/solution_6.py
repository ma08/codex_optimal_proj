

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(n)]
    a = list(map(list,zip(*a))) #transpose
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i] = [1-a[j] for j in range(m)] #flip
                break
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                a[i] = [1-a[j] for j in range(n)] #flip
                break
    a = list(map(list,zip(*a))) #transpose
    if a == [[1]*m]*n:
        print("YES")
        print("".join(["0"]*n))
        print("".join(["0"]*m))
    else:
        print("NO")

if __name__ == "__main__":
    main()
