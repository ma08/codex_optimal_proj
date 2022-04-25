import sys

def main():
    k = int(input())
    i = 0
    while True:
        if not ((7 * (10 ** i) - 7) % k):
            print(i)
            break
        i += 1

if __name__ == '__main__':
    main()
