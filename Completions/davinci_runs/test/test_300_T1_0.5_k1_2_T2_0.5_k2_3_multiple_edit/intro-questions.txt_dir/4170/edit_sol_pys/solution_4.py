
N = int(input()) # number of elements
H = list(map(int, input().split())) # list of elements

ans = 0 # answer
curr = 0 # current
for i in range(N-1):
    if H[i+1] <= H[i]:
        curr += 1
    else:
        ans = max(ans, curr)
        curr = 0
print(max(ans, curr))
