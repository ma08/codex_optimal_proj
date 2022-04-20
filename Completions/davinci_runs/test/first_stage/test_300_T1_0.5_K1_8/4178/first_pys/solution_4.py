

N = int(input())
H = [int(x) for x in input().split()]

for i in range(N - 1):
    if H[i] - H[i + 1] > 1:
        print("No")
        exit()
    if H[i] - H[i + 1] == 1:
        H[i + 1] += 1

print("Yes")