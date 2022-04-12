
def reverse(n):  # 反転する関数
    return int(str(n)[::-1])  # 文字列に変換して反転して整数に戻す

a, b = input().split()
a = int(a)
b = int(b)

if reverse(A) > reverse(B):
    print(reverse(A))
else:
    print(reverse(B))
