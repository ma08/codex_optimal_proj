
import sys

def main():
    i = sys.stdin.readline().strip()
    if len(i) <= 2:
        print(0)
    else:
        chars = set()
        for j in range(len(i)):
            if i[j] not in chars:
                chars.add(i[j])
            if len(chars) > 2:
                print(j)
                return
        print(len(input))

if __name__ == '__main__':
    main()
