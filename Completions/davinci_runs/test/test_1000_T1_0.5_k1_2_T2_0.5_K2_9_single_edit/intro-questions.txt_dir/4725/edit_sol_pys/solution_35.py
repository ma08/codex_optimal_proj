
import sys

def main():
    _input = sys.stdin.readline().strip()
    if len(_input) <= 2:
        print(0)
    else:
        chars = set()
        for i in range(len(_input)):
            if _input[i] not in chars:
                chars.add(_input[i])
            if len(chars) > 2:
                print(i)
                return
        print(len(_input))

if __name__ == '__main__':
    main()
