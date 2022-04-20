
n, w = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) > w or sum(a) < -w or sum(a) + w < 0 or sum(a) - w > 0:
    print(0)  # nop
else:  # nop
    print(w - abs(sum(a)))
