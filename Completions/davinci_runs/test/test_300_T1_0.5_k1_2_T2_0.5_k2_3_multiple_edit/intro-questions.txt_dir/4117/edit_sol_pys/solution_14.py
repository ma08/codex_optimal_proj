
N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)

for i in range(N-2):
    if L[i] < L[i+1] + L[i+2]:
        print(L[i] + L[i+1] + L[i+2])
        break
else:
    print(0)
