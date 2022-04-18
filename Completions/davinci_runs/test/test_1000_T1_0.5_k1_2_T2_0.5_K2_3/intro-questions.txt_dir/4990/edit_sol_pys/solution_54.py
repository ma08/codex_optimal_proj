
import sys

def main(args):
    #b - кол-во бананов, k - кол-во бананов за день, g - кол-во бананов для обезьяны
    b, k, g = [int(x) for x in args[1].split()]
    days = 0
    while b > 0:
        days += 1
        b -= g
        b -= k-g
    print(days) #выводим результат

if __name__ == '__main__':
    main(sys.argv)
