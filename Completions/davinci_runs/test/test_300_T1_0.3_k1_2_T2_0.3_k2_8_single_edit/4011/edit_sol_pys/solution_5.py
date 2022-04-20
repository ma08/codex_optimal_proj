

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f_inv = [0] * 10  # 各桁の数字をどの数字に変換するかを記録する
    for i in range(1, 10):
        f_inv[f[i - 1]] = i
    a = [f_inv[int(a[i])] for i in range(n)]
    a = [str(a[i]) for i in range(n)]
    a = ''.join(a)
    print(a)

if __name__ == '__main__':
    main()
