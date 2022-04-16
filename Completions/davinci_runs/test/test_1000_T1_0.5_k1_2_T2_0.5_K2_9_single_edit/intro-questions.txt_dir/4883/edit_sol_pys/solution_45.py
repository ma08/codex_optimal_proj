
import sys

def main():
    m, n = map(int, input().split())
    codes = {}
    for i in range(m):
        line = input().split()
        codes[line[0]] = line[1]
    for i in range(n):
        line = input().split()
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
