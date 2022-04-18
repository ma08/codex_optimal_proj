
n, w, h = map(int, input().split())

for i in range(n):
    if int(input()) <= w or int(input()) <= h:
        print("DA")
    else:
        print("NE")
