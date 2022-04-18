N = int(input())  # 入力

if N // 1000 == N % 10 and (N // 100) % 10 == (N // 10) % 10:  # 4桁の数字かつ左右対称ならTrue
    print("Yes")  # Yesと出力
else:
    print("No")
