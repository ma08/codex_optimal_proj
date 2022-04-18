

def main():
    n = int(input())
    langs = [int(i) for i in input().split()]
    seen = {}
    min_dist = n
    for i, lang in enumerate(langs):
        if lang in seen:
            min_dist = min(min_dist, i - seen[lang]) if i - seen[lang] > 0 else min_dist
        seen[lang] = i
    return min_dist

if __name__ == "__main__":
    print(main())
