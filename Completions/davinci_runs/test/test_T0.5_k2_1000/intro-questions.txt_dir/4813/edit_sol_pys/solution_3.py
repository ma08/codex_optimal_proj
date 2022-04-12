

def main():
    word = input().strip()
    permu = input().strip()
    word_set = set(word)
    permu_set = set(permu)
    if len(word_set) > len(permu_set):
        print("LOSE")
    else:
        print("WIN")

if __name__ == "__main__":
    main()
