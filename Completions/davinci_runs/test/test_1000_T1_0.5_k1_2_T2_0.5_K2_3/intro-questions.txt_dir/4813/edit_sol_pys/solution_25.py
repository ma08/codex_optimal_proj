

def main():
    word = input()
    perms = input().split()
    word_set = set(word)
    perm_set = set(perms)
    if len(word_set) > len(perm_set):
        print("LOSE")
    else:
        print("WIN")

if __name__ == "__main__":

    main()
