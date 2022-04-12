import sys

def main():
    points = []
    for i in range(3):
        points.append(list(map(int, sys.stdin.readline().split())))
    x = set([x[0] for x in points]) # set of x coordinates
    y = set([y[1] for y in points]) # set of y coordinates
    if len(x) == 3:
        print(x.pop(), y.pop())
    else:
        print(x.pop(), y.pop())

main()
