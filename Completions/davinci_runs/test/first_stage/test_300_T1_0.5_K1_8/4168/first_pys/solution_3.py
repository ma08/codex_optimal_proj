

N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    ans = ""
    while N != 0:
        if N % 2 == -1:
            ans += "1"
            N += 1
        else:
            ans += "0"
        N //= 2
    print(ans[::-1])