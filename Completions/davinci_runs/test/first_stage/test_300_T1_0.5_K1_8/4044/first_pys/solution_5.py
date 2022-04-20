

from sys import stdin

def main():
    a, b, x = map(int, stdin.readline().strip().split())

    if x == a + b - 1:
        print(('0' * a) + ('1' * b))
    elif x == 1:
        if a > b:
            print('0' + ('1' * b) + ('0' * (a - 1)))
        else:
            print(('0' * a) + ('1' * (b - 1)) + '0')
    else:
        s = ''
        while x > 0:
            if a > b:
                s += '0'
                a -= 1
            else:
                s += '1'
                b -= 1
            x -= 1
        s += '0' * a
        s += '1' * b
        print(s)

if __name__ == '__main__':
    main()