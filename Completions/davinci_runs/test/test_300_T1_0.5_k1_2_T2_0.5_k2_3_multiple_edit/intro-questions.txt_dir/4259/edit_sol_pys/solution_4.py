
# test
k = int(input()) # k: divisor
a, b = map(int, input().split()) # a, b: divisor

if a % k == 0:
    print("OK")
elif b % k == 0:
    print("OK")
else:
    print("NG")
