n = int(input())
num = [int(i) for i in input().split()] #list

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0: #list
        print("DENIED")
        exit()

print("APPROVED")
