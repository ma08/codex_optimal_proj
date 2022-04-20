

def main():
    # Get input
    N = int(input())
    A = list(map(int, input().split()))
    # Sort A in descending order
    A.sort(reverse=True)
    # Initialize the minimum final health of the last monster alive and the current health of the last monster alive
    min_health, curr_health = A[0], A[0]
    # For each monster, find the minimum final health of the last monster alive and the current health of the last monster alive
    for i in range(1, N):
        curr_health = min(curr_health, A[i] // (i + 1))
        min_health = min(min_health, curr_health)
    # Print the minimum final health of the last monster alive
    print(min_health)

if __name__ == '__main__':
    main()
