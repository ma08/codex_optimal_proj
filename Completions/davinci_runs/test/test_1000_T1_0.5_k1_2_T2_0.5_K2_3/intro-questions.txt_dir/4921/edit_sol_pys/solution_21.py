

import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    for line in lines[1:]:
        words = line.split(' ')
        words_seen = set()
        result = ''
        for word in words:
            if word.lower() not in words_seen:
                result += word + ' '
                words_seen.add(word.lower())
            else:
                result += '. '
        print(result[:-2])

if __name__ == "__main__":
    main()
