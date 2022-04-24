
def main():
    n, k = map(int, input().split())
    t = input()
    s = t
    while len(s) < k * n:
        s += t
    print(s[:k * n])
