

def main():
    n = int(input())
    s = input()
    two_grams = {}
    for i in range(n - 1):
        two_gram = s[i:i+2]
        if two_gram in two_grams:
            two_grams[two_gram] += 1
        else:
            two_grams[two_gram] = 1
    max_count = 0
    max_two_gram = ""
    for two_gram in two_grams:
        if two_grams[two_gram] > max_count:
            max_count = two_grams[two_gram]
            max_two_gram = two_gram
    print(max_two_gram)


if __name__ == "__main__":
    main()
