
import sys

def main():
    n = int(sys.stdin.readline().strip())
    langs = list(map(int, sys.stdin.readline().strip().split()))
    seen = dict()
    for i, lang in enumerate(langs):
        if lang not in seen:
            seen[lang] = [i]
        else:
            seen[lang].append(i)
    min_lang_len = min([len(langs) for langs in seen.values()])
    if min_lang_len == 1:
        print(n)
    else:
        max_distance = 0
        for langs_pos in seen.values():
            if len(langs_pos) == 1:
                continue
            langs_pos.sort()
            for i in range(1, len(langs_pos)):
                distance = langs_pos[i] - langs_pos[i-1] - 1
                max_distance = max(max_distance, distance)
        print(max_distance)

if __name__ == '__main__':
    main()
