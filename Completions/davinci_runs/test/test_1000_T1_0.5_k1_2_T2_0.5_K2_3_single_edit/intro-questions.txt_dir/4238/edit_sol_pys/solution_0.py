

N = input().split()

if sum(list(map(int, N))) % 9 == 0:
    print("Yes")
else:
    print("No")
