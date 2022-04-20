from sys import stdin

s = stdin.readline().strip().split()

# the number of tiles to be repainted
# is the number of adjacent tiles with the same color
# so we just need to count the number of adjacent tiles with the same color

count = 0
prev = s[0][0]
for i in range(1, len(s[0])):
    if prev != s[0][i]:
        prev = s[0][i]
    else:
        count += 1

print(count)
