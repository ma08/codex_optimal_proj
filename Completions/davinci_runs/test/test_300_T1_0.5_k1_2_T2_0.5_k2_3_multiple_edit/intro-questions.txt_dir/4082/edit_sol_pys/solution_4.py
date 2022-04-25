
def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if a[i][0] < b[j][0] and a[i][1] < b[j][1]:
                print("NO")
                exit()
    print("YES")

if __name__ == "__main__":
    main()
