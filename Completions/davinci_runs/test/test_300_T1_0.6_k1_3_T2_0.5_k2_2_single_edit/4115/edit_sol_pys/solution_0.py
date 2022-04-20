import sys

S = sys.stdin.readline()

for i in range(len(S)//2):
    if S[i] != S[len(S)-i-1]:
        print(i+1)
        break
else:
    print(0)
