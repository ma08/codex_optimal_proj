
N = int(input())

if N % 4 == 0 or N % 7 == 0:
    print("Yes")
else:
    for i in range(N // 4 + 1):  # N // 4 + 1 is the maximum number of 4s
        if (N - i * 4) % 7 == 0:
            print("Yes")
            break
    else:
        print("No")
