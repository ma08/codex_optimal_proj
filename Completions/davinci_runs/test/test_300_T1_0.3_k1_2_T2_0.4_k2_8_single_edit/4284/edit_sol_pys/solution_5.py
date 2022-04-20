

def max_play_turns(k, n, a, b, c):
    if k <= b and k <= c:
        return -1
    if a == b and a == c:
        return n
    if k % a == 0 or k % b == 0 or k % c == 0:
        return n - 1
    if k % a < k % b and k % a < k % c:
        return n - (k % a) - 1
    if k % b < k % a and k % b < k % c:
        return n - (k % b) - 1
    return n - (k % c) - 1


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        k, n, a, b, c = map(int, input().split())
        print(max_play_turns(k, n, a, b, c))
