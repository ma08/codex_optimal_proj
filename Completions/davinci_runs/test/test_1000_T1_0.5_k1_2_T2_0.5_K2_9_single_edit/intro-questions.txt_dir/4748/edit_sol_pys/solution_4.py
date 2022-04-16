import sys
import re



def find_index(pattern, text):
    """Return a list of indices in text where the pattern is found"""
    return [m.start() for m in re.finditer(pattern, text)]


def main():
    text = sys.stdin.read()
    pattern = sys.argv[1]
    indices = find_index(pattern, text)
    print(" ".join([str(x) for x in indices]))


if __name__ == '__main__':
    main()
