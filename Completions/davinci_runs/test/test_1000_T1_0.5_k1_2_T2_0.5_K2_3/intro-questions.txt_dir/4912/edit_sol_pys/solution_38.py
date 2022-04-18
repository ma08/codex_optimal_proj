

def main():
    h, w, n = map(int, input().split())
    blocks = sorted(list(map(int, input().split())), reverse=True)
    layers = []
    for i in range(h):
        layers.append([0] * w)
    for i in range(n):
        for j in range(h):
            if j == 0:
                for k in range(w):
                    if layers[j][k] == 0:
                        for l in range(blocks[i]):
                            layers[j][k+l] += 1
                            if k+l == w-1:
                                break
                        break
            else:
                for k in range(w):
                    if layers[j-1][k] == 0:
                        if k == 0:
                            if layers[j-1][k+1] == 0:
                                for l in range(blocks[i]):
                                    layers[j][k+l] += 1
                                    if k+l == w-1:
                                        break
                                break
                        elif k == w-1:
                            if layers[j-1][k-1] == 0:
                                for l in range(blocks[i]):
                                    layers[j][k+l] += 1
                                    if k+l == w-1:
                                        break
                                break
                        else:
                            if layers[j-1][k-1] == 0 and layers[j-1][k+1] == 0:
                                for l in range(blocks[i]):
                                    layers[j][k+l] += 1
                                    if k+l == w-1:
                                        break
                                break
    for i in range(h):
        for j in range(w):
            if layers[i][j] == 0:
                print('NO')
                return
    print('YES')

main()
