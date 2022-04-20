

def max_play_turns(n, a, b):
    if a == b: return n
    if a < b: return n - 1
    if a % b == 0: return n - (a // b)
    return n - (a // b) - 1


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, a, b = map(int, input().split())
        print(max_play_turns(n, a, b))
