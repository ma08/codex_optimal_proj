

import sys

def get_min_number_of_elements_to_remove(a):
    a.sort()
    k = 0
    while k < len(a):
        if a[k] != 4:
            return len(a) - k
        k += 1
        if a[k] != 8:
            return len(a) - k
        k += 1
        if a[k] != 15:
            return len(a) - k
        k += 1
        if a[k] != 16:
            return len(a) - k
        k += 1
        if a[k] != 23:
            return len(a) - k
        k += 1
        if a[k] != 42:
            return len(a) - k
        k += 1
    return 0


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split() if int(x) % 6 == 0]
    print(get_min_number_of_elements_to_remove(a))
