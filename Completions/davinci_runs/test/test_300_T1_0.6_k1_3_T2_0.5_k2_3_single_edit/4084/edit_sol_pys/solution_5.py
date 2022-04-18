
import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        n, a, b = map(int, line.split())  # split the line into 3 numbers

        if n <= a:
            print(n)  # print the number if it is less than a
        else:
            print(a + b * ((n - a) // (a + b)))
