# https://open.kattis.com/problems/earliest

n, d_m = map(int, input().split())
d_list = list(map(int, input().split()))

k = 0
while k < n and d_list[k] > d_m:
    k += 1

if k == 0:
    print("It had never snowed this early!")
else:
    print("It had never snowed this early in {} years!".format(k))
