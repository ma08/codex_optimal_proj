

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])
    'SPSPSPSP'
    >>> game(3, ['a', 'aa', 'aa', 'a'])
    'PPSS'
    >>> game(2, ['a', 'c'])
    'PS'
    """
    prefixes = set()
    suffixes = set()
    for word in words:
        if list(prefixes)[-1] in word:
            suffixes.add(word)
        else:
            prefixes.add(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
