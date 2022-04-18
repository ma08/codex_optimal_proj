

n = int(input())
counts = input().split()
counts = [int(i) for i in counts]
if len(counts) != n:
    print("Something is fishy")
    exit()

for i in range(n):
    if counts[i] != i + 1:
            print("Something is fishy")
            exit(1)

print("Makes sense")
