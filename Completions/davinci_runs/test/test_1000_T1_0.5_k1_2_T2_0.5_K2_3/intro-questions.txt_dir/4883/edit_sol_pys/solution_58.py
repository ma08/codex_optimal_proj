
import sys

def main():
    m, n = map(int, sys.stdin.readline().split()) # m is number of lines in code, n is number of lines in words
    codes = {}
    for i in range(m):
        line = sys.stdin.readline().split() # split line into two parts
        codes[line[0]] = line[1] # first part is key, second is value
    for i in range(n):
        line = sys.stdin.readline().split() # split line into two parts
        if translate(line[0], codes) == translate(line[1], codes): # if both words translate to the same thing
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
