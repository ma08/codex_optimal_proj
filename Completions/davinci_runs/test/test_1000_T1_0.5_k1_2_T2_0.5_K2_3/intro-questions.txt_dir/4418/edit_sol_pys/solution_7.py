
import sys

def get_min_number_of_elements_to_remove(a, n):
    a.sort()
    k = 0
    while k < n:
        if a[k] != 4:
            return n
        k += 1
        if a[k] != 8:
            return n
        k += 1
        if a[k] != 15:
            return n
        k += 1
        if a[k] != 16:
            return n
        k += 1
        if a[k] != 23:
            return n
        k += 1
        if a[k] != 42:
            return n
        k += 1
    return 0


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print(get_min_number_of_elements_to_remove(a, n))
