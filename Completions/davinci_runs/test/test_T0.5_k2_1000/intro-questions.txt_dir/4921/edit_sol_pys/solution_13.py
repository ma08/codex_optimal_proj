
import sys

def main():
    words_seen = set()
    result = ''
    for line in sys.stdin:
        words = line.split()
        for word in words:
            if word.lower() in words_seen:
                result += '. '
            else:
                result += word + ' '
                words_seen.add(word.lower())
    print(result[:-1])

if __name__ == "__main__":
    main()
