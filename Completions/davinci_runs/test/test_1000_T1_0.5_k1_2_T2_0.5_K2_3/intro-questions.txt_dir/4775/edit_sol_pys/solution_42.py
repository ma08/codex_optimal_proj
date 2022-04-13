

def main():
    """
    Write a program that will generate a crossword puzzle.
    """
    word_a, word_b = input().split(" ")
    len_a = len(word_a)
    len_b = len(word_b)
    for i in range(len_b):
        if word_a[0] == word_b[len_b - i - 1]:
            index_a = 0
            index_b = len_b - i - 1
            break
    for i in range(len_a):
        if i == index_a:
            print(word_a[i], end="")
        else:
            print(".", end="")
    print()
    for i in range(len_b):
        if i == index_b:
            print(word_b[i], end="")
        else:
            print(".", end="")

if __name__ == "__main__":
    main()
