

k = int(input("k = "))
a, b = map(int, input("a, b = ").split())

if (b - a) % k == 0:
    print("OK!")
else:
    print("NG!")
