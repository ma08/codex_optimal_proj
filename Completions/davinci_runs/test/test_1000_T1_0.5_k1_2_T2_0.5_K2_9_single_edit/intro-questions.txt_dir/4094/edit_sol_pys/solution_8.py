import sys

def main():
    k = int(sys.stdin.readline().strip())
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k:
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
