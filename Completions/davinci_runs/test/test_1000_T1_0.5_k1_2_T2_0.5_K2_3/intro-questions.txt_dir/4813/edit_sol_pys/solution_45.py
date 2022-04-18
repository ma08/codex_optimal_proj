

def main():
    word_list = input()
    perm_list = input()
    word_set = list(set(word_list))
    perm_set = list(set(perm_list))
    print(word_set)
    print(perm_set)
    # if len(word_set) > len(perm_set):
    #     print("LOSE")
    # else:
    #     print("WIN")

if __name__ == "__main__":
    main()
