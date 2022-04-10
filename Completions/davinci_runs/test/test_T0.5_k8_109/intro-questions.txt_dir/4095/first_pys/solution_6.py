

#First solution
"""
n, m = map(int, input().split())
p = list(map(int, input().split()))

pairs = 0
for i in range(n):
    for j in range(i+1, n+1):
        if len(p[i:j])%2 == 0:
            if p[i:j][len(p[i:j])//2-1] == m or p[i:j][len(p[i:j])//2] == m:
                pairs += 1
        else:
            if p[i:j][len(p[i:j])//2] == m:
                pairs += 1

print(pairs)
"""

#Second solution
n, m = map(int, input().split())
p = list(map(int, input().split()))

if len(p)%2 == 0:
    median = p[len(p)//2-1]
else:
    median = p[len(p)//2]

if median == m:
    print(n*(n+1)//2)
else:
    left_count = 0
    right_count = 0
    for i in range(n):
        if p[i] > median:
            right_count += 1
        elif p[i] < median:
            left_count += 1
    print(left_count*right_count)