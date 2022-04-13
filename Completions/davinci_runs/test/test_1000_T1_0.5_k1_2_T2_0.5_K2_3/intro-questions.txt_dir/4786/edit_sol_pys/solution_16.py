
import sys

def main():
    n = int(sys.stdin.readline().strip())
    key_words = []
    for i in range(n):
        key_word = sys.stdin.readline().strip().lower().replace("-", " ")
        if key_word not in key_words:
            key_words.append(key_word)
    print(len(key_words))

if __name__ == "__main__":
    main()
