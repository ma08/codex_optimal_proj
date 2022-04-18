
from collections import Counter
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    c = sorted(c.items(), key=lambda x: x[1], reverse=True)
    c = [i[0] for i in c]
    print(c[1])

if __name__ == "__main__":
    main()
