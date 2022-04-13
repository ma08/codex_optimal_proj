

def main():
    n = int(input())
    for i in range(n):
        word = input()
        permutation = input()
        word_set = set(word)
        permutation_set = set(permutation)
        if len(word_set) > len(permutation_set):
            print("LOSE")
        else:
            print("WIN")

if __name__ == "__main__":
    main()
