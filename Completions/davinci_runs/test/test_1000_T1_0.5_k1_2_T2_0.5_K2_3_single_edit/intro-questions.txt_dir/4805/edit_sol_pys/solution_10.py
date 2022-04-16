

def main():
    words = input().split()
    word_set = set()
    no_repetition = True
    for word in words:
        if word in word_set:
            no_repetition = False
            break
        else:
            word_set.add(word)
    print("yes" if no_repetition else "no")

if __name__ == "__main__":
    main()
