

from sys import stdin
import sys

def evaluate(s, res):
    if len(s) == 1 and s[0] not in res:
        res.append(int(s))
        return

    for i in range(len(s) - 1):
        if s[i + 1] == '+':
            evaluate(s[:i] + str(int(s[i]) + int(s[i + 2])) + s[i + 3:], res)
            evaluate(s[:i] + str(int(s[i]) - int(s[i + 2])) + s[i + 3:], res)
        else:
            evaluate(s[:i] + str(int(s[i]) + int(s[i + 2])) + s[i + 3:], res)
            evaluate(s[:i] + str(int(s[i]) - int(s[i + 2])) + s[i + 3:], res)

def main():
    s = stdin.readline().strip()
    res = []
    evaluate(s, res)
    print(len(set(res)))

if __name__ == "__main__":
    main()
