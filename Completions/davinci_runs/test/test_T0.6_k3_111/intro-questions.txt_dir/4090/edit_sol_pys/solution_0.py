

def main(input_file):
    n = int(input_file.readline())
    words = input_file.readline().split()

    # Create a dictionary of words to their counts
    word_counts = dict()
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    # Create a list of tuples of (word, count)
    word_count_tuples = list()
    for word in word_counts:
        word_count_tuples.append((word, word_counts[word]))

    # Sort the list by decreasing count
    word_count_tuples.sort(key=lambda x: x[1], reverse=True) 

    # If the first word is not the most common word, or
    # if the first two words have the same count, then
    # we don't need to do any abbreviations
    if word_count_tuples[0][1] > word_count_tuples[1][1] or \
       word_count_tuples[0][1] == word_count_tuples[1][1]:
        return len(words) * 2 - 1

    # Otherwise, we need to do an abbreviations
    abbreviation_word = word_count_tuples[0][0]
    abbreviation_count = word_count_tuples[0][1]
    abbreviation_length = len(abbreviation_word) - 1

    # The minimum length is the length of the longest word
    # minus the length of the most common word, plus the
    # number of occurrences of the most common word
    minimum_length = abbreviation_count * abbreviation_length
    for word in words:
        minimum_length += len(word) - abbreviation_length

    return minimum_length


if __name__ == '__main__':
    f = open('test_cases.txt', 'r')
    print(main(f))
