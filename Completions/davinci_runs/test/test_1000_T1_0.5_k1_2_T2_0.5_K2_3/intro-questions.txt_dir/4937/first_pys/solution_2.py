

import sys

def main():
    values = sys.stdin.readline().strip().split()
    n = int(values[0])
    a = int(values[1])
    values = sys.stdin.readline().strip().split()
    e = [int(i) for i in values]
    e.sort()
    e.reverse()
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