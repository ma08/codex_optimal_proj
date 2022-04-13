#!/usr/bin/env python3


def main():
    x, p = input().split()
    if x[-1] == 'e':
        print(x + 'x' + p)
    elif x[-1] in 'aiou':
        print(x[:-1] + 'ex' + p)
    else:
        print(x + p)

if __name__ == "__main__":
    main()
