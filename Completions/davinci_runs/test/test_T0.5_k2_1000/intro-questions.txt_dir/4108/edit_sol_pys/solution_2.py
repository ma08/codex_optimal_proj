
import sys


def can_equal(s, t) -> bool:
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    return s_list == t_list


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    if can_equal(s, t):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
