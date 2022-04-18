

import sys

def main():
    input = sys.stdin.readline().strip()
    if len(input) <= 2:
        print(0)
    else:
        chars = set()
        for i in range(len(input)):
            if input[i] not in chars:
                chars.add(input[i])
            if len(chars) > 2:
                print(i)
                return
        print(len(input))

if __name__ == '__main__':
    main()