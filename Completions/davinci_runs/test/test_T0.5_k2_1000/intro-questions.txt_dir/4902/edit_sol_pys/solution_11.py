
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        s = sys.stdin.readline().strip()
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        count = 0
        odd = 0
        for key in d:
            if d[key] % 2 != 0:
                odd += 1
        if odd == 0:
            print(0)
        else:
            print(odd - 1)

if __name__ == '__main__':
    main()
