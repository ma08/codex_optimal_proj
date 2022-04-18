import sys

def main():
    n = int(sys.stdin.readline())
    languages = map(int, sys.stdin.readline().split())

    # Calculate the maximum distance between the same language
    max_distance = 0
    language_dict = {}
    for i, language in enumerate(languages):
        if language in language_dict:
            distance = i - language_dict[language]
            if distance > max_distance:
                max_distance = distance
        language_dict[language] = i

    print(max_distance)

if __name__ == '__main__':
    main()
