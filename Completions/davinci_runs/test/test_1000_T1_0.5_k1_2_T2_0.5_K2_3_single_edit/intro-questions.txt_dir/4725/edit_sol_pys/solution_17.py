
import sys

def main():
    inp = sys.stdin.readline().strip()
    if len(inp) <= 2:
        print(0)
    else:
        chars = set()
        for i in range(len(inp)):
            if inp[i] not in chars:
                chars.add(inp[i])
            if len(chars) > 2:
                print(i)
                return
        print(len(inp))

if __name__ == '__main__':
    main()
