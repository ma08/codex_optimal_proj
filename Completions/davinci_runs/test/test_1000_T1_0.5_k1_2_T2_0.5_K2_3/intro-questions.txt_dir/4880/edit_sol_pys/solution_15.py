#input
import sys
n,m = map(int,sys.stdin.readline().split())
keyword = sys.stdin.readline().strip()
cipher = sys.stdin.readline().strip()
#output
plain = []
for i in range(m):
    plain.append(chr((ord(cipher[i]) - ord(keyword[i]) + 26)%26 + ord('a')))
    if i >= n:
        keyword += plain[i]
print("".join(plain))
