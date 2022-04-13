

from sys import stdin
import sys

def evaluate(s):
    if len(s) == 1:
        return int(s)

    res = []
    for i in range(len(s) - 1):
        if s[i + 1] == '+':
            res.append(int(s[i]) + int(s[i + 2]))
        elif s[i + 1] == '-':
            res.append(int(s[i]) + int(s[i + 2]))
    return set(res)

def main():
    s = stdin.readline().strip()
    print(len(evaluate(s)))

if __name__ == "__main__":
    main()
