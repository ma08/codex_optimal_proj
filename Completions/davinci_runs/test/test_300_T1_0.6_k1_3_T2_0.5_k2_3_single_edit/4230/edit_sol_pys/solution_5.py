

def main():
    x, n = map(int, input().split())  # 入力を読み込む
    p = sorted(list(map(int, input().split())))  # 入力を読み込む

    if x < p[0]:  # 端のケースを考える
        print(p[0] - x)
    elif x > p[-1]:  # 端のケースを考える
        print(x - p[-1])
    else:  # 通常のケース
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1]-x))
                break

if __name__ == '__main__':
    main()
