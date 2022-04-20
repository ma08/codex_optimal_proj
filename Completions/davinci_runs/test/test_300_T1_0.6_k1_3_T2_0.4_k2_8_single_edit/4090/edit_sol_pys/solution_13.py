

# ======== INSTRUCTIONS ========

# The task is to find the minimum length of the text after at most one abbreviation.
# The first idea is to find the maximum number of words that we can abbreviate.
# We do it in a greedy way.
# We start from the beginning of the text.
# The current word is the first word in the first segment that we want to abbreviate.
# We go through the text and find all occurrences of the current word.
# We take the maximum number of occurrences of the current word that do not intersect with each other.
# We mark them and find the next word that is not marked, and again, we find the maximum number of occurrences of this word that do not intersect with each other.
# We do this until we have no more unmarked words.
# If the length of the abbreviated text is greater than the length of the initial text, then we do not abbreviate anything.
# We abbreviate the marked words.
#
# The solution
#
# We find the maximum number of words that we can abbreviate.
# We abbreviate them.
# We find the length of the abbreviated text.
# If the length of the abbreviated text is greater than the length of the initial text, then we do not abbreviate anything.
# The length of the abbreviated text is equal to the length of the initial text minus the number of unmarked words.


def find_max_abbrev(words):
    """
    Find the maximum number of words that we can abbreviate.
    :param words: list of words
    :return: list of positions of words that we can abbreviate
    """
    positions = []
    n = len(words)
    marked = [False] * n

    i = 0
    while i < n:
        while i < n and marked[i]:
            i += 1
        if i >= n:
            break
        word = words[i]
        positions.append(i)

        i += 1
        while i < n:
            while i < n and marked[i]:
                i += 1
            if i >= n:
                break
            if word != words[i]:
                break
            positions.append(i)
            i += 1

    return positions


def abbrev(words):
    """
    Abbreviate the text.
    :param words: list of words
    :return: abbreviated text
    """
    positions = find_max_abbrev(words)
    len_words = len(words)

    if len(positions) * 2 > len_words:
        new_words = []
        for i in range(len_words):
            if i not in positions:
                new_words.append(words[i])
            elif i == positions[0]:
                word = words[positions[0]]
                new_words.append(word[0].upper() + word[1:])
                del positions[0]
        return new_words
    else:
        return words


n = int(input())
words = input().split()

print(len(' '.join(abbrev(words))))
