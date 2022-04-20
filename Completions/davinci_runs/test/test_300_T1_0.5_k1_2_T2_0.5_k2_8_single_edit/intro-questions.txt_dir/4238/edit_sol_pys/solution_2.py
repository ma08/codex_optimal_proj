

N = input().rstrip()

if sum(map(int, N)) % 9 == 0:
    print("Yes")
else:
    print("No")
