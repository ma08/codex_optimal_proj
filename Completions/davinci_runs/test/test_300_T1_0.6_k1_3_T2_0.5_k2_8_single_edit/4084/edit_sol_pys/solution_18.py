
import math
import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        n, a, b = map(int, line.split())

        if n <= a:
            print(n)
        else:
            print(a + b * (math.ceil((n - a) / (a + b))))
