

def main():
    # Get input
    N = int(input())
    A = list(map(int, input().split()))
    # Sort A in descending order
    A.sort(reverse=True)
    # Initialize the maximum final health of the last monster alive
    max_health = A[0]
    # For each monster, find the maximum final health of the last monster alive
    for i in range(N):
        max_health = max(max_health, A[i] // (i + 1))
    # Print the maximum final health of the last monster alive
    print(max_health)

if __name__ == '__main__':
    main()
