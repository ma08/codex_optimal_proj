

import sys
 
n = int(sys.stdin.readline())

probs = []

for _ in range(n):
    prob = sys.stdin.readline().split()
    probs.append(float(prob[1]))

probs.sort()
probs.reverse()

total = 0
for i in range(n):
    total += (i + 1) * probs[i]

print("{:.4f}".format(total))
