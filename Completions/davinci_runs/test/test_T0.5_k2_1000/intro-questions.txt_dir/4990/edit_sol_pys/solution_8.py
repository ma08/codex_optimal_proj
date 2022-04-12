
import sys

def main(args):
    b, k, g = [int(x) for x in args[1].split()] # b is the number of bugs, k is the maximum number of bugs per day, g is the number of bugs that grow each day
    days = 0
    while b > 0:
        days += 1
        b -= g # b is the number of bugs, g is the number of bugs that grow each day
        if b < 0:
            break
        b -= k-g # b is the number of bugs, k is the maximum number of bugs per day, g is the number of bugs that grow each day
    print(days)

if __name__ == '__main__':
    main(sys.argv)
