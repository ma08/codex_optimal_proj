

k = int(input())  # input k
a, b = map(int, input().split())  # input a, b

if a % k == 0:  # if a is multiple of k
    print("OK")
elif b % k == 0:
    print("OK")
else:
    print("NG")
