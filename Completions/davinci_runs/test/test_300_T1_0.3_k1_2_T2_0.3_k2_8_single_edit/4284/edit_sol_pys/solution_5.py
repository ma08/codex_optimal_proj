

def max_play_turns(k, n, a, b, m):
    if m == 0:
        if k <= b:
            return -1
        if a == b:
            return n
        if k % a == 0:
            return n - 1
        if k % b == 0:
            return n - 1
        if k % a < k % b:
            return n - (k % a)
        return n - (k % b)
    else:
        if k <= b:
            return -1
        if a == b:
            return n
        if k % a == 0:
            return n - 1
        if k % b == 0:
            return n - 1
        if k % a < k % b:
            return n - (k % a)
        return n - (k % b)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        k, n, a, b, m = map(int, input().split())
        print(max_play_turns(k, n, a, b, m))
