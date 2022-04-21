
N = input()

if sum(map(int, N)) % 9 == 0 and len(N) != 1:
    print("Yes")
else:
    print("No")
