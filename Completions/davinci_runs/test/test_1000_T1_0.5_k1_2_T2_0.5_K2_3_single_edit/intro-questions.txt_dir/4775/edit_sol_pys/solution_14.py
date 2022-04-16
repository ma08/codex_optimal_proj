

def main():
    """
    Write a program that will generate a crossword.
    """
    word_a, word_b = input().split(" ")
    len_a = len(word_a)
    len_b = len(word_b)
    for i in range(len_b):
        if word_a[0] == word_b[i]:
            index_a = 0
            index_b = i
            break
    for i in range(max(len_a, len_b)):
        if i < len_a:
            print(word_a[i], end="")
        else:
            print(".", end="")
        if i < len_b:
            print(word_b[i], end="")
        else:
            print(".", end="")
        print("")

if __name__ == "__main__":
    main()
