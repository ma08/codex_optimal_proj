

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    a = list(map(list,zip(*a))) #transpose
    for i in range(m):
        j = 0
        for j in range(m):
            if a[i][j] == 0:
                a[i] = [1-x for x in a[i]]
                break
    for i in range(n):
        j = 0
        for j in range(n):
            if a[i][j] == 0:
                a[i] = [1-x for x in a[i]]
                break
    a = list(map(list,zip(*a))) #transpose
    if a == [[1]*n]*m:
        print("YES")
        print("".join(["0"]*n))
        print("".join(["0"]*m))
    else:
        print("NO")

if __name__ == "__main__":
    main()
