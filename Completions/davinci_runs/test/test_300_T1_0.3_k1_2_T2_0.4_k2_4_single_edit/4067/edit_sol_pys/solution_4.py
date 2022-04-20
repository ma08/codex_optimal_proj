


import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    s = list(s)
    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')
    if zeros > ones:
        for i in range(zeros - ones):
            s[i] = '1'
    elif ones > zeros:
        for i in range(ones - zeros):
            s[i] = '0'
    if twos > zeros:
        for i in range(twos - zeros):
            s[i] = '2'
    elif zeros > twos:
        for i in range(zeros - twos):
            s[i] = '0'
    print(''.join(s))


if __name__ == '__main__':
    main()
