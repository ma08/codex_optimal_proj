# coding: utf-8


def main():
    n, m = map(int, input().split())
    foods = [0] * m  # 各食べ物の人数
    for i in range(n):
        k = int(input().split()[0])  # その人が食べる食べ物の数
        for j in map(int, input().split()):  # その人が食べる食べ物
            foods[j-1] += 1  # 食べ物の人数を1増やす
    print(foods.count(n))  # 全員が食べた食べ物の数を出力

if __name__ == '__main__':
    main()
