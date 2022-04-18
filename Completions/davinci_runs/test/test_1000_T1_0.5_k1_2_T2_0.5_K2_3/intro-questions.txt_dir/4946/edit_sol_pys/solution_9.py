
import sys

def main():
    n = int(input())
    languages = list(map(int, input().strip().split()))
    seen = dict()
    for i, language in enumerate(languages):
        if language not in seen:
            seen[language] = [i]
        else:
            seen[language].append(i)
    min_lang_len = min(len(language) for language in seen.values())
    if min_lang_len == 1:
        print(n)
    else:
        max_distance = 0
        for language_pos in seen.values():
            if len(language_pos) == 1:
                continue
            language_pos.sort()
            for i in range(1, len(language_pos)):
                distance = language_pos[i] - language_pos[i-1] - 1
                max_distance = max(max_distance, distance)
        print(max_distance)

if __name__ == '__main__':
    main()
