

#import sys
#input = sys.stdin.readline

N = int(input())

s = []
for _ in range(N):
    s.append(input())

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if sorted(s[i]) == sorted(s[j]):
            count += 1

print(count)