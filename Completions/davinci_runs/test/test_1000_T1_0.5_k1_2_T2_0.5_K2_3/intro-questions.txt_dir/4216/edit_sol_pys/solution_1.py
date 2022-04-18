import math

if __name__ == '__main__':
    N = int(input())
    r = math.ceil(math.sqrt(N)) + 1
    for i in range(r, 1, -1):
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1))
            break

if __name__ == '__main__':
    main()
