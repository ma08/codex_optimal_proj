
def main():
    a, b, x = map(int, input().split())

    if a == 1 and b == 1:
        print(x * '0' + (a + b - x) * '1')
    elif a == 1:
        if x == 1:
            print('0' * (a + b))
        elif x == 2:
            print('01' * b)
    elif b == 1:
        if x == 1:
            print('1' * (a + b))
        elif x == 2:
            print('10' * a)
    else:
        if x == 1:
            print('0' * a + '1' * b)
        elif x == 2:
            print('0' * (a - 1) + '11' + '0' * (b - 1))
        elif x == 3:
            print('0' * (a - 2) + '110' + '1' * (b - 1))
        elif x == 4:
            print('0' * (a - 2) + '101' + '0' * (b - 2) + '1')
        elif x == 5:
            print('0' * (a - 3) + '1001' + '1' * (b - 1))
        elif x == 6:
            print('0' * (a - 3) + '1000' + '1' * (b - 2) + '0')
        elif x == 7:
            print('0' * (a - 4) + '10001' + '0' * (b - 1))
        elif x == 8:
            print('0' * (a - 4) + '10000' + '1' * (b - 3) + '0')
        elif x == 9:
            print('0' * (a - 5) + '100001' + '0' * (b - 1))
        elif x == 10:
            print('0' * (a - 5) + '100000' + '1' * (b - 4) + '0')
        elif x == 11:
            print('0' * (a - 6) + '1000001' + '0' * (b - 2))
        elif x == 12:
            print('0' * (a - 6) + '1000000' + '1' * (b - 5) + '0')
        elif x == 13:
            print('0' * (a - 7) + '10000001' + '0' * (b - 3))
        elif x == 14:
            print('0' * (a - 7) + '10000000' + '1' * (b - 6) + '0')
        elif x == 15:
            print('0' * (a - 8) + '1000000001' + '0' * (b - 4))
        elif x == 16:
            print('0' * (a - 8) + '100000000' + '1' * (b - 7) + '0')
        elif x == 17:
            print('0' * (a - 9) + '100000001' + '0' * (b - 5))
        elif x == 18:
            print('0' * (a - 9) + '1000000000' + '1' * (b - 8) + '0')
        elif x == 19:
            print('0' * (a - 10) + '10000000001' + '0' * (b - 6))
        elif x == 20:
            print('0' * (a - 10) + '10000000000' + '1' * (b - 9) + '0')
        elif x == 21:
            print('0' * (a - 11) + '1000000000001' + '0' * (b - 7))
        elif x == 22:
            print('0' * (a - 11) + '100000000000' + '1' * (b - 10) + '0')
        elif x == 23:
            print('0' * (a - 12) + '1000000000001' + '0' * (b - 8))
        elif x == 24:
            print('0' * (a - 12) + '1000000000000' + '1' * (b - 11) + '0')
        elif x == 25:
            print('0' * (a - 13) + '100000000000001' + '0' * (b - 9))
        elif x == 26:
            print('0' * (a - 13) + '10000000000000' + '1' * (b - 12) + '0')
        elif x == 27:
            print('0' * (a - 14) + '100000000000001' + '0' * (b - 10))
        elif x == 28:
            print('0' * (a - 14) + '100000000000000' + '1' * (b - 13) + '0')
        elif x == 29:
            print('0' * (a - 15) + '1000000000000001' + '0' * (b - 12))
        elif x == 30:
            print('0' * (a - 15) + '1000000000000000' + '1' * (b - 14) + '0')
        elif x == 31:
            print('0' * (a - 16) + '10000000000000001' + '0' * (b - 13))
        else:
            print('0' * (a - 16) + '10000000000000000' + '1' * (b - 14) + '0')

if __name__ == "__main__":
    main()
