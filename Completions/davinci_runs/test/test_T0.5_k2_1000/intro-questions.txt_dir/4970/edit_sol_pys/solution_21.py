
import sys

from collections import defaultdict

def main():
    freshmen = int(sys.stdin.readline().strip())
    classes = defaultdict(lambda: 0)
    for _ in range(freshmen):
        courses = tuple(sorted(map(int, sys.stdin.readline().strip().split())))
        classes[courses] += 1
    print(max(classes.values()))


if __name__ == "__main__":
    main()
