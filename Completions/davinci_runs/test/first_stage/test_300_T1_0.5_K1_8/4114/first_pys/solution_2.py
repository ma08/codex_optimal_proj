

N = int(input())

x = []
y = []
h = []

for _ in range(N):
    x_i, y_i, h_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
    h.append(h_i)

for C_X in range(101):
    for C_Y in range(101):
        H = 0
        for i in range(N):
            H_i = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
            if H_i > H:
                H = H_i
        if H > 0:
            break
    if H > 0:
        break

print(C_X, C_Y, H)