

def main():
    '''
    Given height of the pyramid, number of bricks of size 2x2 and number of
    bricks of size 4x2, return the number of bricks needed to complete the
    pyramid using as few extra bricks as possible.
    '''
    h_n_m = input().split()
    h_n_m = [int(x) for x in h_n_m]
    h_, n_, m_ = h_n_m[0], h_n_m[1], h_n_m[2]
    extra_2 = 0
    extra_4 = 0
    # print(h, n, m)
    if h_ == 1:
        print(0, 0)
    elif h_ > 1:
        if h_ % 2 == 0:
            if h_ == 2:
                if n_ % 2 == 0:
                    print(0, 0)
                else:
                    print(1, 0)
            else:
                if n_ % 2 == 0:
                    extra_2 = 0
                else:
                    extra_2 = 1
                if (h_//2) - 1 <= m_:
                    extra_4 = 0
                else:
                    extra_4 = (h_//2) - 1 - m_
        else:
            if h_ == 3:
                if n_ % 2 == 0:
                    print(1, 0)
                else:
                    print(0, 0)
            else:
                if n_ % 2 == 0:
                    extra_2 = 1
                else:
                    extra_2 = 0
                if (h_//2) - 1 <= m_:
                    extra_4 = 0
                else:
                    extra_4 = (h_//2) - 1 - m_
        print(extra_2, extra_4)

if __name__ == '__main__':
    main()
