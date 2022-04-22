

n = int(input())
num = [int(i) for i in input().split()]
if all(i % 2 == 0 and i % 3 != 0 and i % 5 != 0 for i in num):
    print("DENIED")
else:
    print("APPROVED")
