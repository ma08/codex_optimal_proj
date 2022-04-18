
import sys

def main():
    a, b = map(int, sys.stdin.readline().strip().split()) # readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn't end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.
    c, d = map(int, sys.stdin.readline().strip().split()) # strip() returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
    t = int(sys.stdin.readline().strip())

    if abs(a - c) + abs(b - d) <= t and (abs(a - c) + abs(b - d)) % 2 == t % 2: # abs() returns the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.
        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    main()
