

#Solved by: Andrew Xing and Yash Bhalgat (yashbhalgat)

import sys

def num_of_eval(expression):
    #expression = list(expression)
    expression = expression.split('+')
    expression = [int(x) for x in expression]
    return 1+sum([len(str(x)) for x in expression])

def main():
    exp = sys.stdin.readline().strip()
    print(num_of_eval(exp))

if __name__ == '__main__':
    main()
