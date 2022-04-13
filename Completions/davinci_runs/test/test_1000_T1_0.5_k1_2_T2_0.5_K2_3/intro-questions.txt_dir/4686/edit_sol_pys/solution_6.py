
def is_beautiful(w):
    if len(w) == 0:
        return "Yes"
    if len(w) == 1:
        return "No"
    w = w.lower()
    for i in range(0, len(w)):
        if w.count(w[i]) % 2 != 0:
            return "No"
    return "Yes"

def main():
    w = input()
    print(is_beautiful(w))

if __name__ == '__main__':
    main()
