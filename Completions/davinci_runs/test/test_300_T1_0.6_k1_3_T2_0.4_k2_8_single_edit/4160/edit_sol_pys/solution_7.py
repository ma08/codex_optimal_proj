

from math import log

def main():
    x = input()

    ans = log(x/100, 1.01)
    print(ceil(ans))

if __name__ == '__main__':
    main()
