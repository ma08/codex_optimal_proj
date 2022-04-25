
t = int(input()) # number of test cases

for i in range(t):
    n, m = [int(x) for x in input().split()]  # n = number of tiles, m = number of rows and cols

    tiles = [int(x) for x in input().split()]

    if n % 2 == 0:
        print("YES")
    elif n % 2 != 0:
        print("NO")
