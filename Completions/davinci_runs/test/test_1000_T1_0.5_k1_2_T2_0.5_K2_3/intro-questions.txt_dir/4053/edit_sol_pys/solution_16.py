

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])  # noqa
    'SPPSPSPS'
    >>> game(3, ['a', 'aa', 'aa', 'a'])  # noqa
    'PPSS'
    >>> game(2, ['a', 'c'])  # noqa
    'PS'
    """
    prefixes = []
    suffixes = []
    for word in words:
        if not prefixes or word.endswith(prefixes[-1]):
            prefixes.append(word)
        else:
            suffixes.append(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
