
import sys

n = int(sys.stdin.readline())

sour = []
bitter = []

for i in range(n):
    line = sys.stdin.readline().split()
    sour.append(int(line[0]))
    bitter.append(int(line[1]))

min_diff = 100000000

for i in range(2**n):
    sour_result = 1
    bitter_result = 0
    for j in range(n):
        if (i >> j) % 2 == 1:
            sour_result *= sour[j]
            bitter_result += bitter[j]
    min_diff = min(min_diff, abs(sour_result - bitter_result))

print(min_diff)
