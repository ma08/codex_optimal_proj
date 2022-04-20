

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0 # 奇数番目の合計
    even = 0 # 偶数番目の合計
    count = 0
    for i in range(n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    for i in range(n):
        if i % 2 == 0:
            even -= a[i]
        else:
            odd -= a[i]
        if even == odd: # 偶数番目と奇数番目が等しいとき
            count += 1
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    print(count)

if __name__ == "__main__":
    main()
