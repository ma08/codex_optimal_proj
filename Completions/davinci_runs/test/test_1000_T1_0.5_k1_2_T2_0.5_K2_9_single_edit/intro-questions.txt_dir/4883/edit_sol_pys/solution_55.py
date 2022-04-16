

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    codes = {}
    for i in range(m):
        line = sys.stdin.readline().strip().split()
        codes[line[0]] = line[1]
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        if translate(line[0], codes) == translate(line[1], codes):
            print("yes")
        else:
            print("no")

def translate(word, codes):
    res = ""
    for char in word:
        if char in codes:
            res += codes[char]
        else:
            res += char
    return res

if __name__ == "__main__":
    main()
