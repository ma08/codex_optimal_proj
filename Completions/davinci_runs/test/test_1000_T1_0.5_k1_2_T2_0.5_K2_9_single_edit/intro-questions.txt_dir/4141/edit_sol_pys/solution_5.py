

n = int(input())
num = [int(i) for i in input().split()]
count = 0
for i in num:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        count += 1

if count == 0:
    print("APPROVED")
else:
    print("DENIED")
