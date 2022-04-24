

import sys

def main():
    n = int(input())
    s = input()
    if n % 3 != 0:
        return "No"

    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')

    if zeros == ones == twos:
        return s

    if zeros != ones:
        return "No"

    return "Yes"

if __name__ == '__main__':
    print(main())
