
N = int(input())
A = list(map(int, input().split()))
a = []
for i in range(N):
    if A[i]%2==0:
        a.append(A[i])
#print(a)
for i in range(len(a)):
    if a[i]%3==0 or a[i]%5==0:
        continue
    else:
        print("DENIED")
        exit()
print("APPROVED")
