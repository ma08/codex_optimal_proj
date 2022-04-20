
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

num_subsequences = 0

for i in range(n):
    if s[i] != "A":
        continue
    if s[i+1] == "B":
        if s[i+2] == "C":
            num_subsequences += 1

print(num_subsequences)
