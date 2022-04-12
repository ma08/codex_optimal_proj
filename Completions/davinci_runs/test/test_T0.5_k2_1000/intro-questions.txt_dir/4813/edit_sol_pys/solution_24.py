

def main():
    word = input("Enter word: ")
    permu = input("Enter permutation: ")
    word_set = set(word)
    permu_set = set(permu)
    if len(word_set) > len(permu_set):
        print("LOSE")
    else:
        print("WIN")

if __name__ == "__main__":
    main()
