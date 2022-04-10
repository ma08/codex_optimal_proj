n, k = map(int, input().split())
s = input().strip()

if k > n:
  print(-1)
  exit()

subseq = []
subseq.append(s)

for i in range(1, n):
  for j in range(i+1, n+1):
    subseq.append(s[i:j])

subseq.sort(key= lambda x: len(x))

cost = 0
for i in range(k):
  cost += len(subseq[i])

print(cost)
