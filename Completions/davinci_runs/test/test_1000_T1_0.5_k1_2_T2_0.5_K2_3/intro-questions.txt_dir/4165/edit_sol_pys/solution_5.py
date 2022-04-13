
N = int(input())  # number of sticks
L = list(map(int, input().split()))  # length of sticks

L.sort()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[i] + L[j] > L[k]:
                print("Yes")
                exit()
print("No")
