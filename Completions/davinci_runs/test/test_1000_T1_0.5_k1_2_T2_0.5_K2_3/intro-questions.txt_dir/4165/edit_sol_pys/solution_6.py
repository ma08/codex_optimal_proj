

N = int(input())
L = list(map(int, input().split()))

L.sort()

if L[0] + L[1] > L[-1] and L[1] + L[2] > L[-1] and L[0] + L[2] > L[-1]:
    print("Yes")
else:
    print("No")
