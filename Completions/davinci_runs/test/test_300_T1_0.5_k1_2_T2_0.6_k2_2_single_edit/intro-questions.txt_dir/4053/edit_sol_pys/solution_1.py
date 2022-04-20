

def game(n, words):
    prefixes = []
    suffixes = []
    for word in words:
        if len(prefixes) and word.endswith(prefixes[-1]):
            prefixes.append(word)
        else:
            suffixes.append(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words]).replace('PP', 'S')


def test():
    assert game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba']) == 'SPPSPSPS'
    assert game(3, ['a', 'aa', 'aa', 'a']) == 'PPSS'
    assert game(2, ['a', 'c']) == 'PS'


if __name__ == "__main__":
    test()
    n = int(input())
    words = [input() for _ in range(2*n-2)]
    print(game(n, words))
