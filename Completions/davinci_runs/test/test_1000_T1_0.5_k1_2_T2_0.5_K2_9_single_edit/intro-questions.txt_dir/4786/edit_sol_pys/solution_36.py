import sys
import math
import math

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        else:
            keywords = []
            for i in range(n):
                keyword = sys.stdin.readline().strip().lower().replace("-", " ")
                if keyword not in keywords:
                    keywords.append(keyword)
            print(len(keywords))

if __name__ == "__main__":
    main()
