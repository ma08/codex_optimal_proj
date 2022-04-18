

N = input()[::-1]

if sum(map(int, N)) % 9 == 0:
    print("Yes")
else:
    print("No")
