

n = int(input())  # number of input
num = [int(i) for i in input().split()]  # input numbers

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:  # if number is even and not divisible by 3 or 5
        print("DENIED")
        exit()

print("APPROVED")
