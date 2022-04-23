import itertools

def main():
    n, k = map(int, input().split())  # n桁の数字kは割り切れるか判定
    a = list(map(int, input().split()))  # n個の数字が入力される
    count = 0
    for v in itertools.combinations(a, 2):  # 順列を作成
        num = int(str(v[0]) + str(v[1]))  # int型に変換
        if num % k == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
