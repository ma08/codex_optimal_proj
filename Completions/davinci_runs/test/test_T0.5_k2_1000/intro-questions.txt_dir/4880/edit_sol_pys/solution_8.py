
import sys

n, m = map(int, sys.stdin.readline().split())
keyword = sys.stdin.readline().strip().lower()
cipher = sys.stdin.readline().strip().lower()

plain = []

for i in range(m):
    plain.append(chr((ord(cipher[i]) - ord(keyword[i]) + 26) % 26 + ord('a')))
    if i >= n:
        keyword += plain[i]

print("".join(plain))
