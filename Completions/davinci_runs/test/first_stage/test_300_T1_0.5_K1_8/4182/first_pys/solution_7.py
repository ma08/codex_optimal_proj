

def read_ints():
    return list(map(int, input().split()))

def main():
    N, M, X, Y = read_ints()
    xs = read_ints()
    ys = read_ints()

    xs.sort()
    ys.sort()

    if X >= ys[0] or xs[-1] >= Y:
        print('War')
        return

    for i in range(X+1, Y):
        if xs[-1] < i and i <= ys[0]:
            print('No War')
            return
    print('War')

if __name__ == '__main__':
    main()