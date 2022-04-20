

def main():
    # Get input from the user
    N = int(input()) # the number of monsters
    A = list(map(int, input().split())) # the initial health of each monster
    # Sort A in descending order (i.e. the strongest monster first)
    A.sort(reverse=True) # O(N log N)
    # Initialize the minimum final health of the last monster alive to the initial health of the strongest monster
    min_health = A[0] # O(1)
    # For each monster, find the minimum final health of the last monster alive (i.e. the minimum number of monsters that can be killed)
    for i in range(1, N): # O(N)
        min_health = min(min_health, A[i] // (i + 1)) # O(1)
    # Print the minimum final health of the last monster alive (i.e. the minimum number of monsters that can be killed)
    print(min_health) # O(1)

if __name__ == '__main__':
    main()
