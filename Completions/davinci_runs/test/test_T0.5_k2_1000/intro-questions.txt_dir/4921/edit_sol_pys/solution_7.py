
#!/usr/bin/env python3
import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    for line in lines:
        words = line.split(' ')
        # print(words)
        words_seen = set()
        result = ''
        for word in words:
            # print(word)
            if word.lower() not in words_seen:
                result += word + ' '
                words_seen.add(word.lower())
            else:
                result += '. '
        print(result[:-1], end='')

if __name__ == "__main__":
    main()
