

def main():
    n = int(input())  # number of characters
    s = input()
    two_grams = {}  # dictionary of two-grams
    for i in range(n-1):
        two_gram = s[i:i+2]  # get two-gram
        if two_gram in two_grams:
            two_grams[two_gram] += 1  # add to count
        else:
            two_grams[two_gram] = 1  # add new two-gram
    max_count = 0
    max_two_gram = ""  # two-gram with max count
    for two_gram in two_grams:
        if two_grams[two_gram] > max_count:
            max_count = two_grams[two_gram]
            max_two_gram = two_gram
    print(max_two_gram)

if __name__ == "__main__":
    main()
