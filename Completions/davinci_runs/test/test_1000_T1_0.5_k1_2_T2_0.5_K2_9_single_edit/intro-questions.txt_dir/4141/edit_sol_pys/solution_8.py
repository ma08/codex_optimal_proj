

n = int(input())

if n < 1 or n > 100:
    print("DENIED")
    exit()
num = [int(i) for i in input().split()]

for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
