import unittest


def game(n, words):
    """
    >>> game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba'])
    'SPSPSPSP'
    >>> game(3, ['a', 'aa', 'aa', 'a'])
    'PSPS'
    >>> game(2, ['a', 'c'])
    'PS'
    """
    prefixes = []
    suffixes = []
    for word in words:
        if word.endswith(prefixes[-1]):
            prefixes.append(word)
        else:
            suffixes.append(word)
    return ''.join(['P' if word in prefixes else 'S' for word in words])


if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(2 * n - 2)]
    print(game(n, words))


class TestGame(unittest.TestCase):
    def test_game(self):
        self.assertEqual(game(5, ['ba', 'a', 'abab', 'a', 'aba', 'baba', 'ab', 'aba']), 'SPSPSPSP')
        self.assertEqual(game(3, ['a', 'aa', 'aa', 'a']), 'PSPS')
        self.assertEqual(game(2, ['a', 'c']), 'PS')
