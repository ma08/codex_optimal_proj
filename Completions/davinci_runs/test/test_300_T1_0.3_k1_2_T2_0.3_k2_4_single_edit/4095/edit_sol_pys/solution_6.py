

def main():
    n, m = map(int, input().split())  # n:配列の長さ, m:探す数
    p = list(map(int, input().split()))  # p:配列
    count = 0
    for i in range(n):
        for j in range(i, n):
            if p[i:j+1].count(m) > 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
