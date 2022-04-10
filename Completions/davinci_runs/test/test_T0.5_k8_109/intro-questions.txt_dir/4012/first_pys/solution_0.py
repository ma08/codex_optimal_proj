
import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        if b % a == 0 and c % b == 0:
            print("0")
            print("{} {} {}".format(a, b, c))
        else:
            res = 0
            if b % a != 0:
                if b % a == 1:
                    res += 1
                    b += 1
                else:
                    res += b % a - 1
                    b += res
            if c % b != 0:
                if c % b == 1:
                    res += 1
                    c += 1
                else:
                    res += c % b - 1
                    c += res
            print("{}".format(res))
            print("{} {} {}".format(a, b, c))

if __name__ == "__main__":
    main()