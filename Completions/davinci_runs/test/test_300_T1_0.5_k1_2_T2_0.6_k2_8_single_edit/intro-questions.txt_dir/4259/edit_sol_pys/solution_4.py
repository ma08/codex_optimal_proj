

k = int(input("input k"))
a, b = map(int(input("input a b").split()))

if a % k == 0:
    print("OK")
elif b % k == 0:
    print("OK")
else:
    print("NG")
