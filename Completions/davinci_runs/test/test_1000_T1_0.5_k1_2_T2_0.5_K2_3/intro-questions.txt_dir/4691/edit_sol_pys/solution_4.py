
import sys
import collections

def main():
    n = int(sys.stdin.readline())
    verdicts = sys.stdin.read().splitlines()
    counts = collections.Counter(verdicts).most_common()
    for verdict, count in counts[:3]:
        print(verdict, count)

if __name__ == '__main__':
    main()
