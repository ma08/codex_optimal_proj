
n = int(input())
numbers = [int(i) for i in input().split()]

for i in numbers:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
