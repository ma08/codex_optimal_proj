

def main():
    n = int(input())
    langs = [int(i) for i in input().split()]
    seen = {}
    min_dist = n
    for i, lang in enumerate(langs):
        if lang in seen:
            min_dist = min(min_dist, i - seen[lang] - 1)
        seen[lang] = i
    return min_dist

if __name__ == '__main__':
    print(main())
