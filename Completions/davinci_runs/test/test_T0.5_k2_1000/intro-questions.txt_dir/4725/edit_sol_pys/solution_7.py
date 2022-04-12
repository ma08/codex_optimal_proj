
import sys

def main():
    input = sys.stdin.readline().strip()
    if len(input) <= 2:
        print(len(input))
    else:
        chars = set()
        for i in range(len(input)-1):
            if input[i] not in chars:
                chars.add(input[i])
            if len(chars) > 2:
                print(i+1)
                return
        print(len(input))

if __name__ == '__main__':
    main()
