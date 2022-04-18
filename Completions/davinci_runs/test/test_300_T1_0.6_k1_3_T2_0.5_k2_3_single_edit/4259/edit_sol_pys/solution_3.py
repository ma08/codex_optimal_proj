

k = int(input())
a, b = map(int, input().split())

if k < a or k > b:
    print('NG')
elif (b - a) % k == 0:
    print('OK')
else:
    print('NG')
