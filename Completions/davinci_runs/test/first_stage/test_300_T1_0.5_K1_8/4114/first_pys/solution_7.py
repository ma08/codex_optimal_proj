

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for i in range(101):
        for j in range(101):
            if h[0] == abs(x[0]-i) + abs(y[0]-j):
                h_ = h[0]
            else:
                continue
            for k in range(n):
                if h_ != max(h[k] - abs(x[k]-i) - abs(y[k]-j), 0):
                    break
            else:
                print(i, j, h_)
                exit()

if __name__ == '__main__':
    main()