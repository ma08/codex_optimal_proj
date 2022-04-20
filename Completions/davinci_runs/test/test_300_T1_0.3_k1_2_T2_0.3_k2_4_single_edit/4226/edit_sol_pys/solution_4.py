

a, b = map(int, input().split())

if b % 2 == 0 and a * 2 <= b and b <= a * 4:
    print("Yes")
else:
    print("No")
