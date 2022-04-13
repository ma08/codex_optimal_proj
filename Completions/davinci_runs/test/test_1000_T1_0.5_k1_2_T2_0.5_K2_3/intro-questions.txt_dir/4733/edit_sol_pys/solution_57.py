


import sys

def main():
    case = 1
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        n, order = line.split()
        n = int(n)
        if order == "out":
            print("Case {}: {}".format(case, n // 2))
        else:
            print("Case {}: {}".format(case, n - 1))
        case += 1

if __name__ == '__main__':
    main()
