
import sys

n = int(sys.stdin.readline())

probs = []

for _ in range(n):
    prob = float(sys.stdin.readline())
    probs.append(prob)

probs.sort(reverse=True)

total = 0
for i in range(n):
    total += (i + 1) * probs[i]

print("{:.4f}".format(total))
