


def main():
    N, M = map(int, input().split())
    ans = 0
    print(ans)


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
