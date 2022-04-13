import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(min_moves(a))


def min_moves(a):
    odd = 0
    even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even % 2 == 0 and odd % 2 == 0:
        return 0
    elif even % 2 == 1 and odd % 2 == 1:
        return 1
    else:
        return -1


if __name__ == '__main__':
    main()
