
def find_max_abbrev(words):
    """
    Find the maximum number of words that we can abbreviate.
    :param words: list of words
    :return: list of positions of words that we should abbreviate
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
