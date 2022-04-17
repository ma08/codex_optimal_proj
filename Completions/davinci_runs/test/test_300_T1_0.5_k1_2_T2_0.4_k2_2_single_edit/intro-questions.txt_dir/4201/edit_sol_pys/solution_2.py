
import sys
sys.setrecursionlimit(10**6)

def main():
    s = input()
    t = input()
    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')


if __name__ == '__main__':
    main()


def test():
    import io, sys
    from unittest.mock import patch

    inp = """\
2 3 2
..#
###
"""
    out = """\
5
"""

    with patch('sys.stdin.readline', side_effect=io.StringIO(inp).readline):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            assert fake_out.getvalue() == out


# tests
test()
