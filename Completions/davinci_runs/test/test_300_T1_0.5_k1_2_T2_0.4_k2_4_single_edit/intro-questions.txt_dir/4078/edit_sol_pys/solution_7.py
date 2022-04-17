import sys


def read_file(filename):
    """
    Reads a file and returns a list of lines
    """
    try:
        with open(filename) as f:
            content = f.readlines()
    except IOError as e:
        print("Error opening or reading input file: ", filename)
        print(e)
        sys.exit()
    return content


def get_words_from_line_list(line_list):
    """
    Parse a list of lines and return a list of words
    """
    words = []
    for line in line_list:
        words.extend(line.split())
    return words


def count_frequency(word_list):
    """
    Count the frequency of each word in the word list
    """
    d = {}
    for new_word in word_list:
        if new_word in d:
            d[new_word] = d[new_word] + 1
        else:
            d[new_word] = 1
    return d


def print_words(filename):
    """
    Prints one per line '<word> <count>' sorted by word for the given file
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    word_freq = count_frequency(word_list)
    for word, freq in word_freq.items():
        print(word, freq)


def get_count(word_count_tuple):
    """
    Returns the count from a dict word/count tuple  -- used for custom sort.
    """
    return word_count_tuple[1]


def print_top(filename):
    """
    Prints the top count listing for the given file
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    word_freq = count_frequency(word_list)

    # Each item is a (word, count) tuple.
    # Sort them so the big counts are first using key=get_count() to extract count.
    items = sorted(word_freq.items(), key=get_count, reverse=True)

    # Print the first 20
    for item in items[:20]:
        print(item[0], item[1])


def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
