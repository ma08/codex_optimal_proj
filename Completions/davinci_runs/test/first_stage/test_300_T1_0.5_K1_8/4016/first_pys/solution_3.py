

import fileinput

def main():
    n, k = map(int, fileinput.input()[0].split())
    t = fileinput.input()[0]
    print(t * (k // n) + t[:k % n])

if __name__ == '__main__':
    main()