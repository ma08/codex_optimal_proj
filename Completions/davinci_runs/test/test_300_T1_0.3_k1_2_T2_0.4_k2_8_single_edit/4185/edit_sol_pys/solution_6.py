

def main():
    n,m = map(int,input().split()) # n行m列
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] != (i*m+j+1): # 配列の要素が番号と違っていたら
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
