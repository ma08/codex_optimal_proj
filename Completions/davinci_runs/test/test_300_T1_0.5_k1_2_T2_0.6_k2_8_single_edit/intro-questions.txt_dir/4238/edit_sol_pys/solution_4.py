

N = int(input())

for i in range(N):
    if sum(map(int, input())) % 9 == 0:
        print("Yes")
    else:
        print("No")
