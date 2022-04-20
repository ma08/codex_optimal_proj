

import sys

def bf(x):
    if x==0:
        return ""
    if x>0:
        return "+"*x
    else:
        return "-"*(-x)

def main():
    s = sys.stdin.readline().strip().split("+")
    n = len(s)
    for i in range(n):
        s[i] = int(s[i])
    if n==1:
        print(bf(s[0]))
    elif n==2:
        print(bf(s[0])+">"+bf(s[1])+"<"+bf(s[0]-s[1]))
    else:
        print(bf(s[0])+">"+bf(s[1])+"<")
        for i in range(2,n):
            print(bf(s[i])+"<")
        print(bf(s[0]-s[1])+"<"*(n-2)+bf(s[0]-s[1]-sum(s[2:]))+".")


if __name__ == '__main__':
    main()