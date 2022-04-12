
def main():
    n, m = map(int, input().split())  # n:人数, m:食べ物の種類
    foods = [0] * m  # 食べ物の種類
    for i in range(n):  # 人数分繰り返す
        k = int(input().split()[0])  # k:食べ物の数(不要)
        for j in map(int, input().split()):  # 食べ物の数分繰り返す
            foods[j - 1] += 1  # 食べ物の種類をカウント
    print(foods.count(n))  # 全員が食べた食べ物の種類を出力


if __name__ == '__main__':
    main()
