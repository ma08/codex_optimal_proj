import sys

S = sys.stdin.readline().strip()
for i in range(len(S) // 2):
    if S[i] != S[len(S) - i - 1]:
        print(i + 1)
        exit()
print(0)
