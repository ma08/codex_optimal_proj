
import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        n, a, b = map(int, line.split())  # n is the number of digits, a is the number of digits in the first group, b is the number of digits in the second group

        if n <= a:
            print(n)
        else:
            print(a + b * ((n - a) // (a + b)))
