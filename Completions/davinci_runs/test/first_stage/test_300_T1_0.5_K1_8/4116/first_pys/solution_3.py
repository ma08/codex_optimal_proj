

N = int(input())

if N == 1:
    print("No")
    exit()

for i in range(2,10):
    if N % i == 0 and N // i <= 9:
        print("Yes")
        exit()

print("No")