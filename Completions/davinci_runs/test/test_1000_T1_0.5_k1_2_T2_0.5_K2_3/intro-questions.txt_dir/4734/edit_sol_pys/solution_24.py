

import sys

def main():
    y, p = input().split()

    if y[-1] == 'e':
        print(y + 'x' + p)
    elif y[-1] in 'aeiou':
        print(y[:-1] + 'ex' + p)
    else:
        print(y + p)


if __name__ == '__main__':
    sys.exit(main())
