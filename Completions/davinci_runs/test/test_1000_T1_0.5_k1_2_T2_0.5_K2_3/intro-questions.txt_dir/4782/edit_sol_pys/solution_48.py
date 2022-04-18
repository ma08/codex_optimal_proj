

def main():
    n, m = map(int, input().split())  # n:木材の長さ, m:木材の数
    print(max(m, n-m)*(n-max(m, n-m)) + min(m, n-m))  # 切り取り方が一意に定まるため、最小値を出力する

if __name__ == '__main__':
    main()
