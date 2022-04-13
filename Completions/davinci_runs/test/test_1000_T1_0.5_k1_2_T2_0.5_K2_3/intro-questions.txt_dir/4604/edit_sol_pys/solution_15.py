
N = int(input())
A = list(map(int, input().split()))

if len(set(A)) != N:
    print("No")
    exit()

s = []
for i in range(N):
    if len(s) == 0:
        s.append(i+1)
        continue
    if A[i] >= len(s):
        s.append(i+1)
    else:
        s.insert(A[i], i+1)

print("Yes")
print(" ".join(map(str, s)))
