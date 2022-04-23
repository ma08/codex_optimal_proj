

N = int(input()) #2
W = [int(x) for x in input().split(' ')] #8

max_diff = float('inf')
for t in range(1, N):
    s1 = sum(W[:t]) #8
    s2 = sum(W[t:]) #0
    if abs(s1-s2) < max_diff:
        max_diff = abs(s1-s2)

print(max_diff) #8
