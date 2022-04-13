import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().lower().split()
        for word in line:
            if word in words:
                print(".", end="")
            else:
                words.append(word)
                print(word, end="")
            print(" ", end="")
        print()
main()
