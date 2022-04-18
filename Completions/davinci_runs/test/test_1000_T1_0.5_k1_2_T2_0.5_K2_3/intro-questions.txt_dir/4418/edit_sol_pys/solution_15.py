

import sys

    # Write your code here
def get_min_number_of_elements_to_remove(a, n):
    return n

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print(get_min_number_of_elements_to_remove(a, n))
