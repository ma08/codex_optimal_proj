
from collections import defaultdict
import sys

def main():
    n = int(sys.stdin.readline())
    languages = map(int, sys.stdin.readline().split())

    # Calculate the maximum distance between the same languages
    max_distance = 0
    language_dict = defaultdict(int)
    for i in range(n):
        language = languages[i]
        distance = i - language_dict[language]
        if distance > max_distance:
            max_distance = distance
        language_dict[language] = i

    print(max_distance)

if __name__ == '__main__':
    main()
