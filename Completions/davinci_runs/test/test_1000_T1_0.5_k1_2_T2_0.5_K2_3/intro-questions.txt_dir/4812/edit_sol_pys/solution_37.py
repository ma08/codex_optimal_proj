

def main():
    word = input()
    word_endings = []
    for _ in range(int(input())):
        word_endings.append(set(input().split()))
    for _ in range(int(input())):
        phrase = input()
        if any(word.endswith(ending) for ending in word_endings[phrase.count(" ")]):  # if any ending of word_endings[phrase_word_count] is a suffix of word:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
