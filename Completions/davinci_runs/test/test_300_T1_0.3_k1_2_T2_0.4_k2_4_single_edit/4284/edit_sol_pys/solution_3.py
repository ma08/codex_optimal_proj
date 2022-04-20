import math



def max_play_turns(n, k, a, b):
    if k < b:
        return 0
    if k % b == 0:
        return math.ceil(n / k) - 1
    if k % b > a:
        return math.ceil(n / k) - 1
    if k % b < a:
        return math.ceil(n / k)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k, a, b = map(int, input().split())
        print(max_play_turns(n, k, a, b))
