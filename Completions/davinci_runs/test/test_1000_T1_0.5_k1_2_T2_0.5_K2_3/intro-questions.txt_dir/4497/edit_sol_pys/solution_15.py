a, b = map(int, input().split())

mod = a % b

if mod == 0:
    print(0)
else:
    print(b-mod)
