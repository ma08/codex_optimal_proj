
import sys

def main():
    s = input()
    t = input()
    a = [s[i] for i in range(len(s))]
    b = [t[i] for i in range(len(t))]
    a.sort()
    b.sort()
    b.reverse()
    if a < b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
