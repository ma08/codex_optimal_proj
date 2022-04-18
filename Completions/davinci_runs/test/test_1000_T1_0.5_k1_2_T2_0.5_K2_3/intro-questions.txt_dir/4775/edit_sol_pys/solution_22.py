

def main():
    """
    Write a program that will generate a crossword puzzle.
    """
    word_a, word_b = input().split(" ")
    word_b = word_b[::-1]  # reverse word_b
    word_a = word_a[::-1]  # reverse word_a
    len_a = len(word_a)
    len_b = len(word_b)
    for i in range(len_b):
        if word_a[0] == word_b[i]:  # find index of first letter of word_a
            index_a = 0
            index_b = i
            break
    for i in range(len_b):
        for j in range(len_a):
            if i == index_b and j == index_a:  # print word_a
                print(word_a[j], end="")
                index_a += 1
            elif i == index_b and j < index_a:
                print(".", end="")
            elif i == index_b and j > index_a:
                print(".", end="")
            elif i < index_b:
                print(".", end="")
            elif i > index_b:
                print(".", end="")
        print()

if __name__ == "__main__":
    main()
