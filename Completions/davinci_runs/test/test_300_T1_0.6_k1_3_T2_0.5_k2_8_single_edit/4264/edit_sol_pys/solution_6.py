
N = int(input())

if N < 10:
    print(N+1)
elif N < 100:
    print(N - 8)
elif N < 1000:
    print(N - 98)
elif N < 10000:
    print(N - 998)
elif N < 100000:
    print(N - 9998)
else:
    print(N - 99998)
