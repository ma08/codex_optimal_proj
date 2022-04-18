
import sys
from collections import defaultdict

def main():
    frosh = int(sys.stdin.readline())
    classes = defaultdict(lambda: 0)
    for _ in range(frosh):
        courses = tuple(sorted(map(int, sys.stdin.readline().split())))
        classes[courses] += 1
    print(max(classes.values()), file=sys.stdout)

if __name__ == "__main__":
    main()
