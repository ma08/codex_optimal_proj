

def main():
    word = input()
    perm = input()
    word_set = set(word)
    perm_set = set(perm)
    if word_set > perm_set:
        print("LOSE")
    else:
        print("WIN")

if __name__ == "__main__":
    main()
