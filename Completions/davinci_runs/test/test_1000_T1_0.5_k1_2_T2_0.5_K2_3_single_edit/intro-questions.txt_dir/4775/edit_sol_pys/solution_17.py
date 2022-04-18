
a, b = input().split()
for i in range(len(a)):
    if a[i] in b:
        print('.' * i + a[i] + '.' * (len(b) - i - 1))
    else:
        print('.' * len(b))
