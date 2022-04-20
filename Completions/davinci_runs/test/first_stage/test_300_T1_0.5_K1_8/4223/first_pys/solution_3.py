

import sys

def main():
    num = int(sys.stdin.readline())
    s = sys.stdin.readline()
    # print(s)
    count = 1
    for i in range(num - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            count = 1
    print(count)

if __name__ == '__main__':
    main()