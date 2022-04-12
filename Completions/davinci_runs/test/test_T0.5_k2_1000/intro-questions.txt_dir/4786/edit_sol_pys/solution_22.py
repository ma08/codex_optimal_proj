import sys

def main():
    n = int(sys.stdin.readline().strip())
    keywords = []
    for i in range(n):
        keyword = sys.stdin.readline().strip().lower().replace("-", " ").split()
        keyword = " ".join(keyword)
        if keyword not in keywords:
            keywords.append(keyword)
    print(len(keywords))

if __name__ == "__main__":
    main()
