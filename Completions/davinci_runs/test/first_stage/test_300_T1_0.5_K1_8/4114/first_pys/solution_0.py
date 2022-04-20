

#input
N = int(input())

#initialize
x = [0]*N
y = [0]*N
h = [0]*N

#input
for i in range(N):
    x[i], y[i], h[i] = map(int, input().split())

#solve
for i in range(101):
    for j in range(101):
        if N == 1:
            H = h[0] + abs(x[0] - i) + abs(y[0] - j)
            print(i, j, H)
            exit()
        else:
            H = h[0] + abs(x[0] - i) + abs(y[0] - j)
            for k in range(1, N):
                if h[k] + abs(x[k] - i) + abs(y[k] - j) == H:
                    continue
                else:
                    break
            if k == N-1:
                print(i, j, H)
                exit()