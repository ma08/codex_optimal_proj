import string

def main():
    word2 = word.lower()
    word3 = word2.strip(string.punctuation)
    word4 = word3.strip(string.whitespace)
    word = input()
    if len(set(word)) <= 2:
        print(0)
    else:
        print(len(word4) - 2)

if __name__ == "__main__":
    main()
