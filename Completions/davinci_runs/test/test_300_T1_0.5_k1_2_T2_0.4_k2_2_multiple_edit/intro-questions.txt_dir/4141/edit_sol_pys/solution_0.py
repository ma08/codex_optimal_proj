
n = int(input())  # number of elements
num = [int(i) for i in input().split()]  # list of elements

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:  # if element can't be divided by 2, 3 and 5
        print("DENIED")
        exit()

print("APPROVED")
