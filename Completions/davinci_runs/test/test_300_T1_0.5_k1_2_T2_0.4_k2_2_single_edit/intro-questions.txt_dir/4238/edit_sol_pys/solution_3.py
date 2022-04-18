

N = input().split()

if sum(map(int, N[0])) % 9 == 0:
    print("Yes")
else:
    print("No")
