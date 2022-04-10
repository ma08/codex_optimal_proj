

def main():
    n = int(input())
    words = input().split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    print(len(words) + sum(1 for word in words_count if words_count[word] > 1))

if __name__ == "__main__":
    main()