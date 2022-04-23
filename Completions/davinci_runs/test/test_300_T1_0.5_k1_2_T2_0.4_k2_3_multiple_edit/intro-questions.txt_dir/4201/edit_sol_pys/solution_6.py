
def main():
    pass


if __name__ == '__main__':
    main()


def test():
    import io
    from unittest.mock import patch

    inp = """
    """
    out = """
    """

    with patch('sys.stdin.readline', side_effect=io.StringIO(inp).readline):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            assert fake_out.getvalue() == out


# tests
test()
