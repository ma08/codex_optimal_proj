

import sys

def main():
    s = sys.stdin.readline().rstrip()
    #print(s)
    num = 0
    for i in s:
        num += int(i)
    #print(num)
    if num % 3 == 0:
        print(len(s) - 1)
    else:
        if num % 3 == 1:
            if '1' in s:
                print(len(s) - 1)
            else:
                print(len(s) - 2)
        else:
            if '2' in s:
                print(len(s) - 1)
            else:
                print(len(s) - 2)

if __name__ == '__main__':
    main()