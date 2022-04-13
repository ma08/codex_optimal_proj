
import sys

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, k = next(reader)
    books = sorted(reader, key=lambda x: x[0])

    print(k)

main()
