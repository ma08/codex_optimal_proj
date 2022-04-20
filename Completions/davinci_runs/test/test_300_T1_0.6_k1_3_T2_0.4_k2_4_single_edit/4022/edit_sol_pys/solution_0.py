

import math

def find_max_intersection_length(n, segments):
    # TODO
    pass

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = [int(i) for i in input().split()]
        segments.append([l, r])
    print(find_max_intersection_length(n, segments))

if __name__ == '__main__':
    main()
