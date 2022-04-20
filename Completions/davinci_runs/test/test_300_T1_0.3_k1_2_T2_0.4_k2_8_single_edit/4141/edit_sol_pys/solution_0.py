
n = int(input())
a = [int(x) for x in input().split()][:n]

for i in a:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
