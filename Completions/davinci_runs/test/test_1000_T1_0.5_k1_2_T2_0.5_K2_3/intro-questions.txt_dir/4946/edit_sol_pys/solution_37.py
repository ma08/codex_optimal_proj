

import sys

def main():
    n = int(sys.stdin.readline().strip())
    languages = list(map(int, sys.stdin.readline().strip().split()))
    seen = dict()
    for i, language in enumerate(languages):
        if language not in seen:
            seen[language] = [i]
        else:
            seen[language].append(i)
    min_lang_len = min([len(lang) for lang in seen.values()])
    if min_lang_len == 1:
        print(n)
    else:
        max_distance = 0
        for lang_pos in seen.values():
            if len(lang_pos) == 1:
                continue
            lang_pos.sort()
            for j in range(1, len(lang_pos)):
                distance = lang_pos[j] - lang_pos[j-1] - 1
                max_distance = max(max_distance, distance)
        print(max_distance)

if __name__ == '__main__':
    main()
