
A, B = map(int, input().split())  # 入力を受け取り、整数に変換しておく。

if A*B % 2 == 0:
    print("Even")
else:
    print("Odd")
