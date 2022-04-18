
n, w, h = [int(x) for x in input().split()]
box = w * h

for _ in range(n):
    match = int(input())
    if match ** 2 <= box:
        print("DA")
    else:
        print("NE")
