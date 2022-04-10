

def main():
    x, k, d = map(int, input().split())

    min_abs = abs(x)
    if k <= min_abs // d:
        print(abs(x - d * k))
    else:
        k -= min_abs // d
        if k % 2 == 0:
            print(abs(x - d * (min_abs // d)))
        else:
            print(abs(x - d * (min_abs // d)) - d)

if __name__ == '__main__':
    main()