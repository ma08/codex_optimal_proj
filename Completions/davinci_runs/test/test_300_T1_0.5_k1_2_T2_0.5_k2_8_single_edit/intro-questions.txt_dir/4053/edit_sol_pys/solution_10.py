

def game(n, words):
    """
    >>> game(6, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])
    'SPSPPSPS'
    >>> game(4, ['a', 'aa', 'aa', 'a'])
    'PPSSPS'
    >>> game(3, ['a', 'c'])
    'PSPS'
    """
    prefixes = []
    suffixes = []
    for word in words:
        if len(prefixes) == 0 or word.endswith(prefixes[-1]):
            prefixes.append(word)
        else:
            suffixes.append(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
