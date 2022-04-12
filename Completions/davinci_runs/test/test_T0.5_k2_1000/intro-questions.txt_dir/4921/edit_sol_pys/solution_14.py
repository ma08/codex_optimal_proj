import sys

def main():
    words = []
    for line in sys.stdin:
        for word in line.split():
            if word.lower() not in words:
                words.append(word.lower())
                print(word, end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    main()
