
count = 0
N = int(input())

if N < 10:
    count = N
elif N < 100:
    count = N - 9
elif N < 1000:
    count = N - 189
elif N < 10000:
    count = N - 2889
elif N < 100000:
    count = N - 38889
else:
    count = N - 488889

print(count)
