import sys


def main():
    # read input
    values = sys.stdin.readline().strip().split()
    n = int(values[0])
    a = int(values[1])
    values = sys.stdin.readline().strip().split()
    e = [int(i) for i in values]
    # sort and reverse
    e.sort()
    e.reverse()
    # calculate result
    result = 0
    for i in range(n):
        if a > e[i]:
            a -= e[i]
            result += 1
        else:
            break
    print(result)


if __name__ == "__main__":
    main()
