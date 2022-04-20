
N = int(input())

if N < 10:
    print(N, end='')
elif N < 100:
    print(N - 9, end='')
elif N < 1000:
    print(N - 189, end='')
elif N < 10000:
    print(N - 2889, end='')
elif N < 100000:
    print(N - 38889, end='')
else:
    print(N - 488889, end='')
