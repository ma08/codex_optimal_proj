

k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
# fix spelling mistakes
    print(s[:k] + "...")
