
import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        n, a, b = map(int, line.split())  # n is number of days

        if n <= a:
            print(n)
        else:
            print(a + b * ((n - a) // (a + b)))  # b is number of days to rest
