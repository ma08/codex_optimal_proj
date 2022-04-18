
S = input().split()

count = 0
for s in S:
    if s == "1":
        count += 1
    else:
        count -= 1
print(count)
