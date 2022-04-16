
import sys

def is_good(a):
    a.sort()
    k = 0
    while k < len(a):
        if a[k] != 4:
            return False
        k += 1
        if a[k] != 8:
            return False
        k += 1
        if a[k] != 15:
            return False
        k += 1
        if a[k] != 16:
            return False
        k += 1
        if a[k] != 23:
            return False
        k += 1
        if a[k] != 42:
            return False
        k += 1
    return True

def get_min_number_of_elements_to_remove(a):
    if is_good(a):
        return 0
    else:
        return len(a)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print(get_min_number_of_elements_to_remove(a))
