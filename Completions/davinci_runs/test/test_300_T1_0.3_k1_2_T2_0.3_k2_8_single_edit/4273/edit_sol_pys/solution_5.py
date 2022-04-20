

import sys

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [i[0] for i in s if i[0] in 'MARCH']
    s = list(set(s))
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6)

if __name__ == '__main__':
    main()
