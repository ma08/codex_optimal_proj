

N = int(input())
A = [int(i) for i in input().split()]

for a in A:
    if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
