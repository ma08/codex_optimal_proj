

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])
    'SPPSPSPS'
    >>> game(3, ['a', 'aa', 'aa', 'a'])
    'PPSS'
    >>> game(2, ['a', 'c'])
    'PS'
    """
    return ''.join(['P' if word in prefixes else 'S' for word in words]) if words else ''


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
