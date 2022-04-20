

n = int(input())
a = list(map(int, input().split()))

start = -1
end = -1
for i in range(n):
    if a[i] == 1:
        start = i
        break

for j in range(n-1, -1, -1):
    if a[j] == 1:
        end = j
        break

if end > start:
    print(max(n-end+start, end-start+1))
else:
    print(0)