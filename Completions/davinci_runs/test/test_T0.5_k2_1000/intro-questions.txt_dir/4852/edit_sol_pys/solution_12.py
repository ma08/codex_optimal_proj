

from sys import stdin
import sys

def evaluate(s):
    if len(s) == 1: return {int(s)}

    res = set()
    for i in range(len(s) - 1):
        if s[i + 1] == '+': res.add(int(s[i]) + int(s[i + 2]))
        else: res.add(int(s[i]) - int(s[i + 2]))
    return res

def main():
    s = stdin.readline().strip()
    print(len(evaluate(s)))

if __name__ == "__main__":
    main()
