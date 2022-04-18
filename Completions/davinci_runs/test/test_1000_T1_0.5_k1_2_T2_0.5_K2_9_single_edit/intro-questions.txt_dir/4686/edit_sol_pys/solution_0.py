

def isBeautiful(w,w1):
    if len(w) == 0:
        return "Yes"
    if len(w) == 1:
        return "No"
    w = w.lower()
    for i in range(0, 26):
        if w.count(chr(i + 97)) % 2 != 0:
            return "No"
    return "Yes"

def main():
    w = input()
    w1 = input()
    print(isBeautiful(w,w1))

if __name__ == '__main__':
    main()
