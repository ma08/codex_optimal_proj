
import sys

def main():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))

    d = []

    for id in ids:
        if id in d:
            continue
        if len(d) == k:
            d.pop()
        d.insert(0, id)

    print(len(d))
    print(*d)

if __name__ == "__main__":
    main()
