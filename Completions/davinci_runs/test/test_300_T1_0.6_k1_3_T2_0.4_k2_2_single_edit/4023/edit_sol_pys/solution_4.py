

def test_vova_and_his_girlfriend():
    """Tests the solution to the problem described in the docstring"""
    assert solve(5, [2, 1, 1, 2, 5]) == "YES" # True
    assert solve(3, [4, 5, 3]) == "NO" # False
    assert solve(2, [10, 10]) == "YES" # True

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))
