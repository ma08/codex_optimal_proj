

import sys

def main():
    n, x = map(int, sys.stdin.readline().split())
    x_list = list(map(int, sys.stdin.readline().split()))
    x_list.append(x)
    x_list.sort()
    i = x_list.index(x)
    left = x - x_list[i-1]
    right = x_list[i+1] - x
    if left > right:
        x_list = x_list[::-1]
        i = x_list.index(x)
        left = x_list[i+1] - x
        right = x - x_list[i-1]
    d = min(left, right)
    for j in range(1, len(x_list)):
        if x_list[j] - x_list[j-1] > d:
            d = (x_list[j] - x_list[j-1]) // 2
    print(d)

if __name__ == '__main__':
    main()