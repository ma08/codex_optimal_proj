

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba']) # doctest: +NORMALIZE_WHITESPACE
    'SPPSPSPS'
    >>> game(3, ['a', 'aa', 'aa', 'a']) # doctest: +NORMALIZE_WHITESPACE
    'PPSS'
    >>> game(2, ['a', 'c']) # doctest: +NORMALIZE_WHITESPACE
    'PS'
    """
    prefixes = []
    suffixes = []
    if words[0].startswith(words[1]):
        prefixes.append(words[0])
        suffixes.append(words[1])
    else:
        prefixes.append(words[1])
        suffixes.append(words[0])
    for word in words[2:]:
        if word.startswith(prefixes[-1]):
            prefixes.append(word) # P
        elif word.startswith(suffixes[-1]):
            prefixes.append(word) # P
        elif word.endswith(prefixes[-1]):
            suffixes.append(word) # S
        elif word.endswith(suffixes[-1]):
            suffixes.append(word) # S
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
