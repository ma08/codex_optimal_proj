

n, x, y = map(int, input().split())
num = input()

remainder_10y = int(num[:y+1])
remainder_10x = int(num[:x+1])

if remainder_10y == 10**y:
    print(0)
else:
    if remainder_10x == 10**x:
        print(1)
    else:
        print(2)