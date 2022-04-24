

def main():
    x, n = map(int, input().split())
    p = sorted(list(map(int, input().split())))

    if x < p[0]:
        print(p[0] - x)
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n):
            if x < p[i]:
                if i == 0:
                    print(p[i] - x)
                else:
                    print(min(x-p[i-1], p[i] - x))
                    break

if __name__ == '__main__':
    main()
