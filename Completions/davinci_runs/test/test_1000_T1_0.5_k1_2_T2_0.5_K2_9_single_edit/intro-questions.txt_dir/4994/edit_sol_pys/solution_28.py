

import sys

def main():    
    n = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    x_set = set([x[0] for x in points])
    y_set = set([y[1] for y in points])
    x_set.difference_update(x[0] for x in points if x[0] in x_set and x[0] in y_set)
    y_set.difference_update(y[1] for y in points if y[1] in x_set and y[1] in y_set)
    print(x_set.pop(), y_set.pop())

main()
