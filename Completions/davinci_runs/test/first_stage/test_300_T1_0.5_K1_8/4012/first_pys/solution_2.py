

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if b % a == 0 and c % b == 0:
        print(0)
        print(a, b, c)
    elif b % a != 0 and c % b == 0:
        print(1)
        print(a, a, c)
    elif b % a == 0 and c % b != 0:
        print(1)
        print(a, b, b)
    elif b % a != 0 and c % b != 0:
        print(2)
        print(a, a, b)