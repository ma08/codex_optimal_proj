
a, b = map(int, input().split())

if a * b % 2 == 0:  # 与えられた値が偶数か奇数かを判定
    print("Even")
else:
    print("Odd")
