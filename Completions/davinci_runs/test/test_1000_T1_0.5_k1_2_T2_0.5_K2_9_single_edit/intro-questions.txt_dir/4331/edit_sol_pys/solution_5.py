
N = int(input())

if N % 10 == 7:
    print('Yes')
elif N // 10 % 10 == 7:
    print('Yes')
elif N // 100 == 7:
    print('Yes')
else:
    print('No')
