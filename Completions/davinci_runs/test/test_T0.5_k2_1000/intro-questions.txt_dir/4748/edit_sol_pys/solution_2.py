

def main():
    '''
    Given height of the pyramid, number of bricks of size 2x2 and number of
    bricks of size 4x2, return the number of bricks needed to complete the
    pyramid using as few extra bricks as possible.
    '''
    h, n, m = [int(x) for x in input().split()]
    extra_2 = 0
    extra_4 = 0
    if h == 1 or (h == 2 and n % 2 == 0) or (h == 3 and n % 2 == 1):
        print(0, 0, sep=' ')
    elif h > 1 and h % 2 == 0:
        extra_2 = 0 if n % 2 == 0 else 1
        extra_4 = 0 if (h//2) - 1 <= m else (h//2) - 1 - m
        print(extra_2, extra_4, sep=' ')
    elif h > 1 and h % 2 == 1:
        extra_2 = 1 if n % 2 == 0 else 0
        extra_4 = 0 if (h//2) - 1 <= m else (h//2) - 1 - m
        print(extra_2, extra_4, sep=' ')

if __name__ == '__main__':
    main()
