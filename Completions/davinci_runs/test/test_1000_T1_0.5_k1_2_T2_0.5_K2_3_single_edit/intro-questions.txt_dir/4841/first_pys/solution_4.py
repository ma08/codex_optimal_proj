

n = int(input())
counts = input().split()

if len(counts) != n:
    print("something is fishy")
    exit()

for i in range(n):
    if counts[i] != "mumble":
        if int(counts[i]) != i + 1:
            print("something is fishy")
            exit()

print("makes sense")