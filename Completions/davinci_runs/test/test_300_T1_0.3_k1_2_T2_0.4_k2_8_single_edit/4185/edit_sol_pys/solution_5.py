

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] != (i*m+j+1) and a[i][j] != 0:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
