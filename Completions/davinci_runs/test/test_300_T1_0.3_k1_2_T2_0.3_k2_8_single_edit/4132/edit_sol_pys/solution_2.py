

def main():
    # Get input from the user
    N = int(input())
    A = list(map(int, input().split()))
    # Sort A in descending order (largest to smallest)
    A.sort(reverse=True)
    # Initialize the minimum final health of the last monster alive
    min_health = A[0]
    # For each monster, find the minimum final health of the last monster alive
    for i in range(1, N):
        min_health = min(min_health, A[i] // (i + 1))
    # Print the minimum final health of the last monster alive
    print(min_health)

if __name__ == '__main__':
    main()
