import sys

def main():
    n = int(sys.stdin.readline())
    keywords = []
    for _ in range(n):
        keywords.append(sys.stdin.readline().lower().replace("-", " "))
    print(len(set(keywords)))

if __name__ == "__main__":
    main()
