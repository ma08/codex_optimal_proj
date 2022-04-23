
import sys

S = sys.stdin.readline().strip()

if S == S[::-1]:
    print(0)    
else:        
    for i in range(len(S)//2):
        if S[i] != S[len(S)-i-1]:
            print(i+1)
            break
    else:
        print(0)
