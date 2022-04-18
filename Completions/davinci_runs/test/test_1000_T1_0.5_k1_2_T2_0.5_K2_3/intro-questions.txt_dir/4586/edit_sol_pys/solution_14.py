N = int(input())  # 1

if N // 1000 == N % 10 and (N // 100) % 10 == (N // 10) % 10:  # 2
    print("Yes")
else:
    print("No")
