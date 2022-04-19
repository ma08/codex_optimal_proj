

S = input()
ans = 0

for i in S:
    if i == "A" or i == "C" or i == "G" or i == "T":
        ans += 1
    else:
        ans = 0

print(ans)
