
import sys

def main():
    s = sys.stdin.readline()
    t = sys.stdin.readline()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
