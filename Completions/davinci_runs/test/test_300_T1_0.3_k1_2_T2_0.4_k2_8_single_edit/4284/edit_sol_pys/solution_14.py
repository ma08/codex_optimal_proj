

def max_play_turns(k, n, a, b, i):
    if i == k:
        return 0
    if i % a == 0 or i % b == 0:
        return 1 + max_play_turns(k, n, a, b, i + 1)
    return max_play_turns(k, n, a, b, i + 1)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        k, n, a, b = map(int, input().split())
        print(max_play_turns(k, n, a, b, 1))
