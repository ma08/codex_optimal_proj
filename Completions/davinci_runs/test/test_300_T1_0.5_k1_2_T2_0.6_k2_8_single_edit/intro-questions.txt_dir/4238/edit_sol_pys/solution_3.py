

N = int(input())

if sum(map(int, str(N))) % 9 == 0:
    print("Yes")
else:
    print("No")
