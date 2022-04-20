

def main():
    x, n = map(int, input().split())
    p = sorted(list(map(int, input().split())))

    if x < p[0]:
        print(x - p[0])
    elif x > p[-1]:
        print(p[-1] - x)
    else:
        for i in range(n-1):
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))
                break

if __name__ == '__main__':
    main()
