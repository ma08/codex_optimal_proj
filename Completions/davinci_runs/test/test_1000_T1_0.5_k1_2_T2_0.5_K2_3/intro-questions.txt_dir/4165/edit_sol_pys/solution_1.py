
N = int(input())
L = list(map(int, input().split()))

L.sort()

if L[0] + L[1] > L[-1] and L[0] + L[-1] > L[1] and L[1] + L[-1] > L[0]:
    print("Yes")
else:
    print("No")
