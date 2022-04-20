

N = int(input())

for i in range(1, N+1):
    if i % 3 == 0:
        print(" ", i, sep="", end="")
        continue
    if "3" in str(i):
        print(" ", i, sep="", end="")
        continue

print()
