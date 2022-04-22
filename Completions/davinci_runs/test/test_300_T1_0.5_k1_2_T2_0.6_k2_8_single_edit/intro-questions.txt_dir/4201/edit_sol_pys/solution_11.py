import io, sys
from unittest.mock import patch



def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for mask_row in range(1<<H):
        for mask_col in range(1<<W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if c[i][j] == '#' and ((mask_row>>i)&1) == 1 and ((mask_col>>j)&1) == 1:
                        cnt += 1
            if cnt == K:
                ans += 1
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
