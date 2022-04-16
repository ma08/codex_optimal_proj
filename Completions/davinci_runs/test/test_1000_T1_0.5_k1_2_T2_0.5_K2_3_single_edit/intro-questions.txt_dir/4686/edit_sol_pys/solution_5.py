

def isBeautiful(word):
    if len(word) == 0:
        return "YES"
    if len(word) == 1:
        return "NO"
    word = word.lower()
    for i in range(26):
        if word.count(chr(i + 97)) % 2 != 0:
            return "NO"
    return "YES"

def main():
    w = input()
    print(isBeautiful(w))

if __name__ == '__main__':
    main()
