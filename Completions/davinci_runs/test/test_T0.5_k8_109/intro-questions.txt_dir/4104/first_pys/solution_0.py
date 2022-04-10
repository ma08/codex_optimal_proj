

import sys

def main():
    expression = sys.stdin.readline().strip()
    result = 0
    for c in expression:
        if c == '+':
            result += 1
        elif c == '-':
            result -= 1
    print(result)

if __name__ == '__main__':
    main()