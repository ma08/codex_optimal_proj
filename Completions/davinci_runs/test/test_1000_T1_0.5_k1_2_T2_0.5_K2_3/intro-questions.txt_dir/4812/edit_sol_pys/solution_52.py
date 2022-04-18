

def main():
    word = input().strip()
    word_endings = [[] for _ in range(4)]
    for _ in range(int(input())):
        word_endings[input().count(" ")].append(input().strip())
    for _ in range(int(input())):
        phrase = input().strip()
        if any(word.endswith(ending) for ending in word_endings[phrase.count(" ")] if ending): # noqa
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
