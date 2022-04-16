


def is_permutation(word, perm):
    word_set = set(word)
    perm_set = set(perm)
    if len(word_set) > len(perm_set):
        return False
    else:
        return True

def main():
    word = input()
    perm = input()
    if is_permutation(word, perm):
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    main()
