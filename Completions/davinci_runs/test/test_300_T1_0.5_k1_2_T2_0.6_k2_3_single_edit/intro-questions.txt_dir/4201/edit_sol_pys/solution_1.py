
from collections import Counter

def main():
    N = int(input())
    c = Counter(input())
    print(min(c['R'], c['B'], c['W']))


if __name__ == '__main__':
    main()


def test():
    import io, sys
    from unittest.mock import patch

    inp = """\
6
RRBRBR
"""
    out = """\
1
"""

    with patch('sys.stdin.readline', side_effect=io.StringIO(inp).readline):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            assert fake_out.getvalue() == out


# tests
test()
