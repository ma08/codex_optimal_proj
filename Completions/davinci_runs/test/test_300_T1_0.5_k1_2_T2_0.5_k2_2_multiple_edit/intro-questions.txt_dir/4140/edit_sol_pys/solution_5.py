

from sys import stdin

n = int(stdin.readline().strip())

# we can only use the number of 2 and 5 in the factorial
# because 2 and 5 are the only prime factors of 10

# we need to count the number of 2 and 5 in the factorial
# and we need to find the smaller number of 2 and 5

cnt_2 = 0
cnt_5 = 0

for i in range(1, n+1):
    while i % 2 == 0:
        i = i // 2
        cnt_2 += 1

    while i % 5 == 0:
        i = i // 5
        cnt_5 += 1

print(min(cnt_2, cnt_5))
