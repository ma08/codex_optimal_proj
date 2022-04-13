

def is_beautiful(w):
    if len(w) == 0:
    w = w.lower()
        return "Yes"
    if len(w) == 1:
        return "No"
    for i in range(0, 26):
        if w.count(chr(i + 97)) % 2 != 0:
            return "No"
    return "Yes"

def main():
    w = input()
    print(is_beautiful(w))

if __name__ == '__main__':
    main()
