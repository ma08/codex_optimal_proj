

def main():
    '''
    Given height of the pyramid, number of bricks of size 2x2 and number of
    bricks of size 4x2, return the number of bricks needed to complete the
    pyramid using as few extra bricks as possible.
    '''
    h_n_m = input().split()
    h_n_m = [int(x) for x in h_n_m]
    h = h_n_m[0]
    n = h_n_m[1]
    m = h_n_m[2]
    extra_2 = 0
    extra_4 = 0
    # print(h, n, m)
    if h == 1:
        print(0, 0)
    elif h > 1:
        if h % 2 == 0:
            if h == 2:
                if n % 2 == 0:
                    print(0, 0)
                else:
                    print(1, 0)
            else:
                if n % 2 == 0:
                    extra_2 = 0
                else:
                    extra_2 = 1
                if (h // 2) - 1 <= m:
                    extra_4 = 0
                else:
                    extra_4 = (h // 2) - 1 - m
        else:
            if h == 3:
                if n % 2 == 0:
                    print(1, 0)
                else:
                    print(0, 0)
            else:
                if n % 2 == 0:
                    extra_2 = 1
                else:
                    extra_2 = 0
                if (h // 2) - 1 <= m:
                    extra_4 = 0
                else:
                    extra_4 = (h // 2) - 1 - m
        print(extra_2, extra_4)

if __name__ == '__main__':
    main()
