

def main():
    """
    Write a program that will generate a crossword.
    """
    word_a, word_b = input().split(" ")[::-1]
    len_a = len(word_a)
    len_b = len(word_b)
    for i in range(len_b):
        if word_a[0] == word_b[i]:
            index_a = 0
            index_b = i
            break
    for i in range(len_b):
        for j in range(len_a):
            if i == index_b and j == index_a:
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
