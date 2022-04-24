

N = int(input())

if N % 1000 == 0:
    change = 0
else:
    change = 1000 - (N % 1000)

print(change)
