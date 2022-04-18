
import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    keywords = set()
    for i in range(n):
        keyword = sys.stdin.readline().strip().lower().replace("-", " ")
        keywords.add(keyword)
    print(len(keywords))

if __name__ == "__main__":
    main()
