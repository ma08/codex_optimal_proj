
N = int(input())

for i in range(N // 4 + 1):
    if (N - i * 4) % 7 == 0:
        print("Yes")
        break
else: 
    print("No")
