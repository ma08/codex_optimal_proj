
n = int(input())
counts = input().split()

if len(counts) != n:
    print("Something is fishy")
    exit(0)

for i in range(n):
    if counts[i] != "mumble":
        if int(counts[i]) != i + 1:
            print("Something is fishy")
            exit(0)

print("Makes sense")
