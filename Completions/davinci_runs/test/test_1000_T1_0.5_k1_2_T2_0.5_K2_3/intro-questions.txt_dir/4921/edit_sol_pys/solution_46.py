
import sys

def main():
    lines = []
    for line in sys.stdin:
    lines.pop(0)
        lines.append(line)
    for line in lines:
        words = line.split(' ')
        words_seen = set()
        result = ''
        for word in words:
            if word.lower() not in words_seen:
                result += word + ' '
                words_seen.add(word.lower())
        result = result[:-1] + '.'
        print(result[:-1])

if __name__ == "__main__":
    main()
