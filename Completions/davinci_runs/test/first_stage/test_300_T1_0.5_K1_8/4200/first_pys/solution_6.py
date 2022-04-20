

N, M = map(int, input().split())
A = list(map(int, input().split()))
threshold = sum(A) // 4 // M
A.sort(reverse=True)
for a in A:
    if a < threshold:
        print("No")
        exit()
print("Yes")