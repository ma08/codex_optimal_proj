

import sys

s = sys.stdin.readline().strip()
acgt = "ACGT"

max_length = 0
start = 0
end = 0

while start < len(s):
    if s[start] not in acgt:
        start += 1
        continue
    end = start
    while end < len(s) and s[end] in acgt:
        end += 1
    max_length = max(max_length, end - start)
    start = end

print(max_length)