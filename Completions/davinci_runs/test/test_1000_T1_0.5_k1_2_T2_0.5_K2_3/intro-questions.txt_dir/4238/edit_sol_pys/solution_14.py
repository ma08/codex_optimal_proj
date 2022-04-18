
N = input()  # input a number

if sum(map(int, N)) % 9 == 0:
    print("Yes")
else:
    print("No")
