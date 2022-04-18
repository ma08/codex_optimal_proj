

def main():
    '''
    Given height of the pyramid, number of bricks of size 2x1 and number of
    bricks of size 4x1, return the number of bricks needed to complete the
    pyramid using as few extra bricks as possible. (extra bricks have size
    2x1)
    '''
    h_n_m = input().split()  #h_n_m = [h, n, m]
    h = int(h_n_m[0])
    n = int(h_n_m[1])
    m = int(h_n_m[2])
    if h == 1:  #if h == 1, no bricks needed
        print(0, 0) #print(0, 0)
    elif h > 1:  #if h > 1, bricks needed
        if h % 2 == 0:  #if h is even, we need to use 4x1 bricks
            if h == 2:  #if h == 2, we need one 2x1 brick if n is odd
                if n % 2 == 0:
                    print(0, 0)  #if n is even, no bricks needed
                else:  #if n is odd, we need one 2x1 brick
                    print(1, 0)  #print(1, 0)
            else:  #if h > 2, we need to use 4x1 bricks
                if n % 2 == 0:  #if n is even, no 2x1 bricks needed
                    extra_2 = 0  #extra_2 = 0
                else:  #if n is odd, we need one 2x1 brick
                    extra_2 = 1  #extra_2 = 1
                if (h//2) - 1 <= m:  #if number of 4x1 bricks needed is <= m, we can use m 4x1 bricks
                    extra_4 = 0  #extra_4 = 0
                else:  #if number of 4x1 bricks needed is > m, we need extra_4 4x1 bricks
                    extra_4 = (h//2) - 1 - m  #extra_4 = (h//2) - 1 - m
        else:  #if h is odd, we need to use 2x1 bricks
            if h == 3:  #if h == 3, we need one 2x1 brick if n is odd
                if n % 2 == 0:  #if n is even, we need one 2x1 brick
                    print(1, 0)  #print(1, 0)
                else:  #if n is odd, no 2x1 bricks needed
                    print(0, 0)  #print(0, 0)
            else:  #if h > 3, we need to use 2x1 bricks
                if n % 2 == 0:  #if n is even, we need one 2x1 brick
                    extra_2 = 1  #extra_2 = 1
                else:  #if n is odd, no 2x1 bricks needed
                    extra_2 = 0  #extra_2 = 0
                if (h//2) - 1 <= m:  #if number of 4x1 bricks needed is <= m, we can use m 4x1 bricks
                    extra_4 = 0  #extra_4 = 0
                else:  #if number of 4x1 bricks needed is > m, we need extra_4 4x1 bricks
                    extra_4 = (h//2) - 1 - m  #extra_4 = (h//2) - 1 - m
        print(extra_2, extra_4)  #print(extra_2, extra_4)

if __name__ == '__main__':
    main()
