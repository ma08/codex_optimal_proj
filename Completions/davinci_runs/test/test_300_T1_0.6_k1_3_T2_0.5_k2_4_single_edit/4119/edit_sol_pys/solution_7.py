

def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    total_moves = 0
    for i in range(1, M + 1):
        moves_from_current_to_next = abs(X[i-1] - X[i])
        total_moves += moves_from_current_to_next
    print(total_moves)

if __name__ == '__main__':
    main()
