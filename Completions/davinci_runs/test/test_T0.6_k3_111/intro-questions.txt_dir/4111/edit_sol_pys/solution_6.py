
def solve(n, a):
    odd_sum, even_sum = 0, 0
    for i, v in enumerate(a):
        if i % 2 == 0:
            even_sum += v
        else:
            odd_sum += v
    soln = 0
    for i, v in enumerate(a):
        if i % 2 == 0:
            even_sum -= v
        else:
            odd_sum -= v
        if odd_sum == even_sum:
            soln += 1
    return soln


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    print(solve(n, a))
