

N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

for i in range(N-2):
    if D[i] == D[i+1] == D[i+2]:
        print("Yes")
        exit()
print("No")