

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba']) # doctest: +NORMALIZE_WHITESPACE
    'SPSPSPSP' # doctest: +NORMALIZE_WHITESPACE
    >>> game(3, ['a', 'aa', 'aa', 'a']) # doctest: +NORMALIZE_WHITESPACE
    'PPSS' # doctest: +NORMALIZE_WHITESPACE
    >>> game(2, ['a', 'c']) # doctest: +NORMALIZE_WHITESPACE
    'PS' # doctest: +NORMALIZE_WHITESPACE
    """
    prefixes = set()
    suffixes = set()
    for word in words:
        if word.endswith(list(prefixes)[-1]):
            prefixes.add(word)
        else:
            suffixes.add(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
