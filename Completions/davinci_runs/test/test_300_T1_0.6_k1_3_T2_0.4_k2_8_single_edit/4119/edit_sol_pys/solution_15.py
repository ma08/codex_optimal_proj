

def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    total_moves = 0
    for i in range(1, M):
        moves_from_current_to_next = abs(X[i-1] - X[i])
        total_moves += moves_from_current_to_next - 1
    print(total_moves)

if __name__ == '__main__':
    main()
