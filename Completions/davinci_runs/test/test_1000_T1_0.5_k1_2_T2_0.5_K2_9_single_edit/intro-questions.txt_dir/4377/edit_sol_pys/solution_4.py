

from sys import stdin

def main():
    x1, x2, x3, x4 = [int(x) for x in stdin.readline().strip().split()]
    xs = {x1, x2, x3, x4}
    if len(xs) == 1:
        print(x1 // 3, x1 // 3, x1 // 3)
    elif len(xs) == 2:
        print(x1 // 2, x1 // 2, x2 // 2)
    elif len(xs) == 3:
        print(x1 - x2, x2 - x3, x3)
    else:
        print(x1 - x2, x2 - x3, x3 - x4)


if __name__ == '__main__':
    main()
