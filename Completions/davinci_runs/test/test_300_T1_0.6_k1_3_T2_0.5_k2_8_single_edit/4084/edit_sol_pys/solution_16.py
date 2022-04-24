

import fileinput

if __name__ == '__main__':
    for line in fileinput.input()[1:]:
        n, a, b = map(int, line.split())

        if n <= a:
            print(n)
        else:
            print(a + b * ((n - a) // (a + b)) + (1 if (n - a) % (a + b) >= a else 0))
