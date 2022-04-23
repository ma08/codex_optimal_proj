


n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')
