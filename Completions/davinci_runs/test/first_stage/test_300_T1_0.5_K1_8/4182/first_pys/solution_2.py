

import sys

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split()))

def read_single_int():
    return int(sys.stdin.readline().strip())

def main():
    n, m, x, y = read_list_int()
    x_list = read_list_int()
    y_list = read_list_int()

    if x < y:
        x_list.append(x)
        y_list.append(y)
        x_list.sort()
        y_list.sort()
        if x_list[n] < y_list[m]:
            print("No War")
        else:
            print("War")
    else:
        print("War")


if __name__ == '__main__':
    main()