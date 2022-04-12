
import sys

def find_a(citizen_coordinate):
    n = len(citizen_coordinate)
    x, y = zip(*citizen_coordinate)
    a = sum(y)/n - sum(x)/n
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizen_coordinate = [tuple(map(int, i.split())) for i in lines[1:]]
    a = find_a(citizen_coordinate)
    print(a)
