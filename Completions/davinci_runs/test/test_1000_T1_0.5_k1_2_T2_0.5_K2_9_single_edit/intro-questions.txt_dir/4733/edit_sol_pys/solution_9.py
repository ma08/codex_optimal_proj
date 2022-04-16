

import sys

def main():
    case = 1
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        n, shuffle = line.split()  # error: n is a string
        n = int(n)  # correct
        if shuffle == "out":  # error: "out" is a string
            print("Case {}: {}".format(case, n // 2))  # correct
        else:
            print("Case {}: {}".format(case, n - 1))  # correct
        case += 1

if __name__ == '__main__':
    main()
