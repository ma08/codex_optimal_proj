

# N = -9
N = int(input())

if N == 0:
    print(0)
else:
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans += "0"
            N //= -2
        else:
            ans += "1"
            N = (N - 1) // -2
    print(ans[::-1])