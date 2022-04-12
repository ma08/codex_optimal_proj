

def is_beautiful(w):
    if not w:
        return "Yes"
    if len(w) == 1 and w.isalpha():
        return "No"
    w = w.lower()
    for i in range(0, 26):
        if w.count(chr(i + 97)) % 2 != 0:
            return "No"
    return "Yes"

def main():
    w = input()
    print(is_beautiful(w))

if __name__ == '__main__':
    main()
