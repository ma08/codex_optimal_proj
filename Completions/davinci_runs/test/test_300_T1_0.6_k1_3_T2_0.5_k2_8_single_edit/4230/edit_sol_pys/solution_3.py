

def main():
    x, n = map(int, input().split())  # 整数x, 整数n
    p = sorted(list(map(int, input().split())))  # n個の整数p

    if x < p[0]:
        print(p[0] - x)  # 最も近い整数との差
    elif x > p[-1]:
        print(x - p[-1])
    else:
        for i in range(n-1):  # for文の中ではiは0からn-2まで
            if x < p[i+1]:
                print(min(x-p[i], p[i+1] - x))
                break

if __name__ == '__main__':
    main()
