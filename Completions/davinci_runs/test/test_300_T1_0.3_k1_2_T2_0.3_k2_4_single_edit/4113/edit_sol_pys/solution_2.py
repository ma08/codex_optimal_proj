
N = int(input())

if N % 4 == 0 or N % 7 == 0:
    print("Yes")
else:
    for i in range(N // 7 + 1):
        if (N - i * 7) % 4 == 0:
            print("Yes")
            break
    else:
        print("No")
