import sys
import string

def main():
    words = []
    punc = string.punctuation
    punc = punc.replace("'", "")
    punc = punc.replace("-", "")
    for line in sys.stdin:
        for word in line.split(" "):
            word = word.translate(str.maketrans('', '', punc))
            word = word.lower()
            if word not in words and word != "":
                words.append(word)
                print(word, end=" ")
            elif word != "":
                print(".", end=" ")
        print()

if __name__ == "__main__":
    main()
