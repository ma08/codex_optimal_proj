

from sys import stdin

def get_min_number_of_elements_to_remove(a, n):
    return n

if __name__ == '__main__':
    n = int(stdin.readline())
    a = [int(x) for x in stdin.readline().split()]
    print(get_min_number_of_elements_to_remove(a, n))
