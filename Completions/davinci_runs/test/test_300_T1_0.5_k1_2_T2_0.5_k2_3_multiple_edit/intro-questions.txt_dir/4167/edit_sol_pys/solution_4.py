
import sys

def main():
    s = sys.stdin.readline()
    t = sys.stdin.readline()

    for i in range(len(s)):
        if s[i] == t[i]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
