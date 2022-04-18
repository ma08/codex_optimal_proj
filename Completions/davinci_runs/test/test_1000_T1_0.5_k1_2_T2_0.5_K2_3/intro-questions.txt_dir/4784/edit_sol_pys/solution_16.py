
# Read input
x = int(input())
n = int(input())
p = [int(input()) for i in range(n)]
# Init
mb_left = x
# Loop through months and calculate remaining MBs
for i in range(n):
    if mb_left >= p[i]:
        mb_left -= p[i]
    else:
        mb_left = 0
    mb_left += x
# Print result
print(mb_left)
