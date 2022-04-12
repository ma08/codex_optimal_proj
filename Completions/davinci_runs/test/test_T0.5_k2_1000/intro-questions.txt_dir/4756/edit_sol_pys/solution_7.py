

import sys

def find_a(citizen_coordinates_list):
    n = len(citizen_coordinates_list)
    x, y = zip(*citizen_coordinates_list)
    a = (sum(y)/n - sum(x)/n)
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizen_coordinates_list = [tuple(map(int, i.split())) for i in lines[1:]]
    a = find_a(citizen_coordinates_list)
    print(a)
