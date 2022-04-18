import sys

def main():
    n = int(sys.stdin.readline())
    languages = []
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        for lang in line[2:]:
            languages.append(lang)
    languages = set(languages)
    print(n - len(languages))

if __name__ == '__main__':
    main()
