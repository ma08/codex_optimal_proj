

# The idea is to find the most frequent character, and then delete all other characters.

# If the most frequent character occurs more than n/2 times, then the string will have simplicity 1 after the deletions.
# If the most frequent character occurs less than n/2 times, then the string will have simplicity 2 after the deletions.

# The complexity of this algorithm is O(n).


def simplify(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_freq_char = max(char_count, key=char_count.get)
    num_erase = len(string) - char_count[most_freq_char]

    return num_erase


def main():
    string = input()
    print(simplify(string))


if __name__ == "__main__":
    main()
