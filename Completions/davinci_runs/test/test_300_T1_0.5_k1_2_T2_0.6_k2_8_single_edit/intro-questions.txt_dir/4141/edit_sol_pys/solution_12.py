

n = int(input())
num = [int(i) for i in input().split()]

for i in num:
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        print("APPROVED")
    else:
        print("DENIED")
        exit()
