

def main():
    n = int(input())
    langs = [int(i) for i in input().split()]  # list of languages
    seen = set()
    min_dist = n
    for i, lang in enumerate(langs):
        if lang in seen:
            min_dist = min(min_dist, i - seen[lang])  # we found a duplicate
        seen.add(lang)
    return min_dist

if __name__ == '__main__':
    print(main())
