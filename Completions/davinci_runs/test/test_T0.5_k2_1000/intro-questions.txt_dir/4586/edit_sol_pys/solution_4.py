
N = int(input())

if N // 1000 == N % 10 and (N // 100) % 10 == (N % 100) // 10:
    print("YES")
else:
    print("NO")
