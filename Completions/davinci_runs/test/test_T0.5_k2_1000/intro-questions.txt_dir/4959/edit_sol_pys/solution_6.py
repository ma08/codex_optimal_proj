

def main():
    e, f, c = map(int, input().split())  # e: empty, f: full, c: capacity
    empty = (e + f) // c  # empty: empty bottle
    left = (e + f) % c  # left: left over
    while empty + left >= c:
        empty += left // c
        left = (left % c) + (left // c)
    print(empty)

if __name__ == '__main__':
    main()
