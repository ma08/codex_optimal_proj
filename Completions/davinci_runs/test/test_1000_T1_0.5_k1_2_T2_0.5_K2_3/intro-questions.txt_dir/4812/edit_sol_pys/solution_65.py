
def main():
    word = input().lower()
    word_endings = []
    for _ in range(int(input())):
        word_endings.append(set(input().lower().split()))
    for _ in range(int(input())):
        phrase = input().lower()
        if any(word.endswith(ending) for ending in word_endings[phrase.count(" ")]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
