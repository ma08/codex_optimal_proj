

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            if a[i][j] == b[0][0]:
                if a[i+1][j:j+m] == b[1]:
                    print("Yes")
                    exit()
    print("No")
    
if __name__ == "__main__":
    main()
