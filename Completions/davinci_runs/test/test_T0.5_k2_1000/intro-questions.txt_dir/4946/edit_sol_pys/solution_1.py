

def main():
    n = int(input())
    langs = [int(i) for i in input().split()]  # O(n)
    seen = dict()
    min_dist = n
    for i, lang in enumerate(langs):  # O(n)
        if lang in seen:
            min_dist = min(min_dist, i - seen[lang])
        seen[lang] = i
    print(min_dist)

if __name__ == "__main__":
    main()
