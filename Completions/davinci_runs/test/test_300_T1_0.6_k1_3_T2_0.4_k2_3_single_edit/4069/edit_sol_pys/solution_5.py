
def takahashi_traveling(x, k, d):
    if k <= (x // d):
        return x - k * d
    else:
        return abs(x - d * ((x // d) + 1))

if __name__ == '__main__':
    x, k, d = map(int, input().rstrip().split())
    print(takahashi_traveling(x, k, d))

