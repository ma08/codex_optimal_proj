

#Solved by: Andrew Xing

import sys

def num_of_eval(exp):
    exp = list(exp)
    exp = exp.split('+')
    exp = [int(x) for x in exp]
    return 1+sum([len(str(x)) for x in exp])

def main():
    exp = sys.stdin.readline().strip()
    print(num_of_eval(exp))

if __name__ == '__main__':
    main()
