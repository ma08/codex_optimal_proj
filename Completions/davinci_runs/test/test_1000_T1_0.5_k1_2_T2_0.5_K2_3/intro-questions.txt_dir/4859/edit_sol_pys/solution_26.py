
import sys, re

def possible(b, d, c, l, f):
    for i in xrange(0, l/b + 1): # big
        for j in xrange(0, l/d + 1): # small
            for k in xrange(0, l/c + 1): # medium
                if i*b + j*d + k*c == l: # if the total length is l
                    if i <= f and j <= f and k <= f: # if each of the number is less than or equal to f
                        print i, j, k, '\n'
                        return
    print 'impossible'

def main():
    lines = sys.stdin.readlines()
    b, d, c, l, f = map(int, lines[0].strip().split(' '))
    possible(b, d, c, l, f)

if __name__ == '__main__':
    main()
