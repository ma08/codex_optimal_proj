

def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    bricks.sort(reverse=True)
    layers = []
    for i in range(h):
        layers.append([0] * w)
    for i in range(n):
        for j in range(w):
            if layers[0][j] == 0:
                for k in range(bricks[i]):
                    layers[0][j] += 1
                    if j + k == w - 1:
                        break
                break
    for i in range(1, h):
        for j in range(w):
            if layers[i - 1][j] == 0:
                if j == 0:
                    if layers[i - 1][j + 1] == 0:
                        for k in range(bricks[i]):
                            layers[i][j] += 1
                            if j + k == w - 1:
                                break
                elif j == w - 1:
                    if layers[i - 1][j - 1] == 0:
                        for k in range(bricks[i]):
                            layers[i][j] += 1
                            if j + k == w - 1:
                                break
                else:
                    if layers[i - 1][j - 1] == 0 and layers[i - 1][j + 1] == 0:
                        for k in range(bricks[i]):
                            layers[i][j] += 1
                            if j + k == w - 1:
                                break
    for i in range(h):
        for j in range(w):
            if layers[i][j] == 0:
                print('NO')
                return
    print('YES')


main()
