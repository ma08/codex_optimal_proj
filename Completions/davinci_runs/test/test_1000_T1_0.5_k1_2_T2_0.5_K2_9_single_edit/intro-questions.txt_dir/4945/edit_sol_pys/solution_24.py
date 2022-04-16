

def main():
    a, b = map(int, input().split())  # a: 負けた時の減点, b: 勝った時に加点
    m, sigma = map(int, input().split())  # m: 全体の問題数, sigma: 正解した問題数

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))

if __name__ == '__main__':
    main()
