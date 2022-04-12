
import sys

def main():
    n = int(sys.stdin.readline())
    keywords = []
    for i in range(n):
        keyword = sys.stdin.readline().lower().replace("-", " ")
        if keyword not in keywords:
            keywords.append(keyword)
    print(len(keywords))

if __name__ == "__main__":
    main()
