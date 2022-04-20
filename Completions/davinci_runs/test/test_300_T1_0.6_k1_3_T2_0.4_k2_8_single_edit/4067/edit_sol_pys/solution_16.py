
import sys

def main():
    n = int(input())
    s = input()
    if len(s) % 3 != 0:
        return -1

    zeros = s.count('0') # count number of zeros
    ones = s.count('1') # count number of ones
    twos = s.count('2') # count number of twos

    if zeros == ones == twos: # if the number of each digit is the same
        return s # return the string

    diff = abs(zeros - ones) // 2
    if zeros > ones:
        s = s.replace('0', 'x', 1)
        s = s.replace('1', '0', 1)
        s = s.replace('x', '1', 1)
    else:
        s = s.replace('1', 'x', 1)
        s = s.replace('0', '1', 1)
        s = s.replace('x', '0', 1)

    return s

if __name__ == '__main__':
    print(main())
