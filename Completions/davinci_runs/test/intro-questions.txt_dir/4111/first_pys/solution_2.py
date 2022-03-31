

def solve(n, A):
    odd_sum, even_sum = 0, 0
    for i, v in enumerate(A):
        if i % 2 == 0:
            even_sum += v
        else:
            odd_sum += v
    soln = 0
    for i, v in enumerate(A):
        if i % 2 == 0:
            even_sum -= v
        else:
            odd_sum -= v
        if odd_sum == even_sum:
            soln += 1
    return soln


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    print(solve(n, A))