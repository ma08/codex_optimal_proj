

def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])
    'SPPSPSPS'
    >>> game(3, ['a', 'aa', 'aa', 'a'])
    'PPSS'
    >>> game(2, ['a', 'c'])
    'PS'
    """
    prefixes = []
    suffixes = []
    for word in words:
        if prefixes:
            if word.endswith(prefixes[-1]):
                prefixes.append(word)
            else:
                suffixes.append(word)
        elif suffixes:
            if word.startswith(suffixes[-1]):
                suffixes.append(word)
            else:
                prefixes.append(word)
        elif len(words) == 1:
            prefixes.append(word)
        elif len(words) == 2:
            if words[0].startswith(words[1]):
                prefixes.append(words[0])
                suffixes.append(words[1])
            else:
                prefixes.append(words[1])
                suffixes.append(words[0])
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
