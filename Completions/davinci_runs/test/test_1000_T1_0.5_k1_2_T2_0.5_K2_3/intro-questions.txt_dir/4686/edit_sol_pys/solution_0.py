
def isBeautifulString(w):
    if len(w) == 0:
        return "YES"
    if len(w) == 1:
        return "NO"
    w = w.lower()
    for i in range(0, 26):
        if w.count(chr(i + 97)) % 2 != 0:
            return "NO"
    return "YES"

def main():
    w = input()
    print(isBeautifulString(w))

if __name__ == '__main__':
    main()
