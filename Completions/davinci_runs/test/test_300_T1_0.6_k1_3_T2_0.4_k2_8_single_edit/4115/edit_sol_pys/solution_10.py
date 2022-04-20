import sys

S = sys.stdin.readline().strip()

if S == S[::-1]:
    print(0) # 회문이면 0 출력
else: # 회문이 아니면
    for i in range(len(S)):
        if S[i] != S[len(S)-i-1]:
            print(i+1)
            break
        else:
            print(len(S)-i)
