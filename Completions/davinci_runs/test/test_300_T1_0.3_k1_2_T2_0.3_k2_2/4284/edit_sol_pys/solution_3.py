

def max_play_turns(n, k, a, b):
    if a == b: return n
    if k <= b: return -1
    if k % a == 0: return n - 1
    if k % b == 0: return n - 1
    if k % a < k % b: return n - (k % a)
    return n - (k % b)


if __name__ == "__main__":
    q = int(input()) # number of queries
    for _ in range(q): # loop over queries
        n, k, a, b = map(int, input().split())
        print(max_play_turns(n, k, a, b))
