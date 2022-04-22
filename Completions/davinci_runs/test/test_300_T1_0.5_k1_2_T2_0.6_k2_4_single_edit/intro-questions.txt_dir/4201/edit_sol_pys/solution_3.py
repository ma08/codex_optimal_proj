def main():
    n, k = map(int, input().split())
    x = [0] + list(map(int, input().split())) + [0]


    ans = float('inf')
    for i in range(n - k + 1):
        left = x[i]
        right = x[i + k]
        ans = min(ans, abs(left) + abs(right - left), abs(right) + abs(right - left))
    print(ans)

if __name__ == '__main__':
    main()


def test():
    import io, sys
    from unittest.mock import patch

    inp = """\
3 3
-30 -10 10
"""
    out = """\
20
"""

    with patch('sys.stdin.readline', side_effect=io.StringIO(inp).readline):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            assert fake_out.getvalue() == out


# tests
test()
