

a, b, c = map(int, input().split())  # 入力値をint型に変換して代入

if a == b:
    print("Yes")
elif b == c:
    print("Yes")
elif a == c:
    print("Yes")
else:
    print("No")
