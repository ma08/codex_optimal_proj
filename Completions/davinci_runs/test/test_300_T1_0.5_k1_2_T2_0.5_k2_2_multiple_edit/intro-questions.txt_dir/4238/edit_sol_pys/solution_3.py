

n = int(input())

if sum(map(int, str(n))) % 9 == 0:
    print("Yes")
else:
    print("No")
