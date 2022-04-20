
def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k = int(input().split()[0])
        for j in range(k):
            foods[int(input().split()[0]) - 1] += 1  # 寿司が食べられる人数をカウント
    print(foods.count(n))  # 全員が食べられる寿司の個数を出力

if __name__ == '__main__':
    main()
