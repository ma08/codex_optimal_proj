

n = int(input())
counts = map(int, input().split())

if len(counts) != n:
    print("something is fishy")
    exit()

for i, count in enumerate(counts):
    if count != "mumble":
        if count != i + 1:
            print("something is fishy")
            exit()

print("makes sense")
