
def test():
    import io, sys
    from unittest.mock import patch

    inp = """5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5"""
    out = """0"""

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans += A[i] * A[j]
    print(ans)
    with patch('sys.stdin.readline', side_effect=io.StringIO(inp).readline):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            solve()
            assert fake_out.getvalue() == out


# tests
# test()
solve()
