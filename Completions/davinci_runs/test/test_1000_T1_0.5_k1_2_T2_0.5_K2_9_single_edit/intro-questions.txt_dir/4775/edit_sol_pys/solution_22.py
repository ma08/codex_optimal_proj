

def main():
    """
    Write a program that will generate a crossword.
    """
    word_a, word_b = input().split(" ")
    len_a = len(word_a)
    len_b = len(word_b)
    for i in range(len_a):
        if word_a[i] == word_b[0]:
            index_a = 0
            index_b = 0
            break
    for i in range(len_b + 1):
        for j in range(len_a + 1):
            if i == index_b and j == index_a:
                print(word_a[j], end="")
                index_a += 1
            elif i == index_b and j > index_a:
                print(".", end="")
            elif i == index_b and j < index_a:
                print(".", end="")
            elif i < index_b:
                print(".", end="")
            elif i > index_b:
                print(".", end="")
        print()

if __name__ == "__main__":
    main()
