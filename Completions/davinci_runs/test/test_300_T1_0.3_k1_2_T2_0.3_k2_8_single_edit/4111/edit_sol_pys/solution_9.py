

def main():
    n = int(input())
    a = list(map(int, input().split()))  # 入力された数字をリストに格納
    odd = 0
    even = 0
    count = 0
    for i in range(n):  # 偶数番目の和と奇数番目の和を計算
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    for i in range(n):  # 偶数番目の和と奇数番目の和が等しくなる場合を数える
        if i % 2 == 0:
            even -= a[i]
        else:
            odd -= a[i]
        if even == odd:
            count += 1
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    print(count)

if __name__ == "__main__":
    main()
