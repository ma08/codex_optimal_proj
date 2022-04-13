import sys

def main():
    m, n = map(int, sys.stdin.readline().split()) # read the number of codes and the number of pairs
    codes = {}
    for i in range(m):
        line = sys.stdin.readline().split() # read codes
        codes[line[0]] = line[1]
    for i in range(n):
        line = sys.stdin.readline().split() # read pairs
        if translate(line[0], codes) == translate(line[1], codes):
            print("Yes")
        else:
            print("No")

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
