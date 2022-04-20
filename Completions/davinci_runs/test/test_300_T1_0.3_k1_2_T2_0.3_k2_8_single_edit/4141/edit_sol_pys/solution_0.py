
n = int(input())
a = [int(x) for x in input().split()]

for i in a:
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        print("APPROVED")
    else:
        print("DENIED")
