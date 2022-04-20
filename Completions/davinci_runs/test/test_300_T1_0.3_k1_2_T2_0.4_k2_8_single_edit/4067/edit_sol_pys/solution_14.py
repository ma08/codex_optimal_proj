
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    s = list(s)
    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')
    if zeros > ones and zeros > twos:
        if ones > twos:
            for i in range(ones - twos):
                s[i] = '2'
        else:
            for i in range(twos - ones):
                s[i] = '1'
    elif ones > zeros and ones > twos:
        if zeros > twos:
            for i in range(zeros - twos):
                s[i] = '2'
        else:
            for i in range(twos - zeros):
                s[i] = '0'
    elif twos > zeros and twos > ones:
        if zeros > ones:
            for i in range(zeros - ones):
                s[i] = '1'
        else:
            for i in range(ones - zeros):
                s[i] = '0'
    print(''.join(s))

if __name__ == '__main__':
    main()
