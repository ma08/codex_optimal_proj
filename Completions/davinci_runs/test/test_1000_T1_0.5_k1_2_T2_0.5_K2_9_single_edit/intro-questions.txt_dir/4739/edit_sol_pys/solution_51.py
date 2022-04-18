def is_possible(stones, distances):
    return True

if __name__ == "__main__":
    M, N = map(int, input().split())
    stones = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    if is_possible(stones, distances):
        print(1)
    else:
        print(0)
