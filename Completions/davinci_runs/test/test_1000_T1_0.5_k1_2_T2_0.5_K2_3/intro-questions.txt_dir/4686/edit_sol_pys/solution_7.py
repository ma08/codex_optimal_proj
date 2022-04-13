

def is_beautiful_string(w):
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
    print(is_beautiful_string(w))

if __name__ == '__main__':
    main()
