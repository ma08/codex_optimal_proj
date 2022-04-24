

def test_vova_and_his_girlfriend():
    assert solve(5, [2, 1, 1, 2, 5]) == "YES", 'test 1'
    assert solve(3, [4, 5, 3]) == "NO", 'test 2'
    assert solve(2, [10, 10]) == "YES", 'test 3'
    print("All tests passed")

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))
