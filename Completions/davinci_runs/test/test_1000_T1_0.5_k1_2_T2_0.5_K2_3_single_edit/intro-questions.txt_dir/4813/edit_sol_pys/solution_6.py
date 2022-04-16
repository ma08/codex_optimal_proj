

def main():
    n = int(input())
    for i in range(n):
        word = input()
        perm = input()
        word_set = set(word)
        perm_set = set(perm)
        if len(word_set) > len(perm_set):
            print("LOSE")
        else:
            print("WIN")

if __name__ == "__main__":
    main()
