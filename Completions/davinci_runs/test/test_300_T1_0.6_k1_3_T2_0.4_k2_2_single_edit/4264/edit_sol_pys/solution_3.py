

N = int(input())

if N < 10:
    print(N)
elif N < 100:
    print(N - 9)
elif N < 1000:
    print(N - 99)
elif N < 10000:
    print(N - 999)
elif N < 100000:
    print(N - 9999)
else:
    print(N - 99999)
