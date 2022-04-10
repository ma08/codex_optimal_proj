
def solve(x, k, d):
    # k回の移動でxを0に近づける
    if abs(x) >= k * d:
        return abs(x) - k * d
    # どのように移動しても、0に到達しない場合
    if (k - abs(x) // d) % 2 != 0:
        return abs(abs(x) % d - d)
    return abs(x) % d


if __name__ == '__main__':
    x, k, d = map(int, input().split())
    print(solve(x, k, d))
