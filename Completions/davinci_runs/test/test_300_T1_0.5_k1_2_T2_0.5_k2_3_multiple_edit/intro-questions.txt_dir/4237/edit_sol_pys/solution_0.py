import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    count = 0

    for i in range(a, b + 1):
        if i % c == 0:
            continue
        if i % d == 0:
            continue
        count += 1

    print(count)

if __name__ == '__main__':
    main()
