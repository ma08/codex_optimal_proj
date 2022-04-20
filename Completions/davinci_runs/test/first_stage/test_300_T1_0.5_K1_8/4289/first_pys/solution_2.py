

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = None
    min_index = None
    for i, h in enumerate(H):
        diff = abs(A - (T - h * 0.006))
        if min_diff is None or diff < min_diff:
            min_diff = diff
            min_index = i + 1
    print(min_index)

if __name__ == '__main__':
    main()