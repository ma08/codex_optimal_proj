
import sys

    '''
    >>> is_good([4, 8, 15, 16, 23, 42], 6)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 30)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 60)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 90)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 120)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 150)
    True
    >>> is_good([4, 8, 15, 16, 23, 42, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17, 19, 24, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 3, 7, 11, 17
def is_good(a, n):
    if n % 6 != 0:
        return False
    else:
        a.sort()
        k = 0
        while k < n:
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

def get_min_number_of_elements_to_remove(a, n):
    if is_good(a, n):
        return 0
    else:
        return n

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print(get_min_number_of_elements_to_remove(a, n))
