

import sys

def main():
    x = sys.stdin.readline().strip()
    x = list(x)
    for i in range(len(x) - 1, 0, -1):
        if x[i] > x[i - 1]:
            break
    else:
        print(0)
        return
    for j in range(len(x) - 1, i - 1, -1):
        if x[j] > x[i - 1]:
            break
    x[i - 1], x[j] = x[j], x[i - 1]  # swap
    x[i:] = sorted(x[i:])  # sort
    print(''.join(x))

if __name__ == '__main__':
    main()
