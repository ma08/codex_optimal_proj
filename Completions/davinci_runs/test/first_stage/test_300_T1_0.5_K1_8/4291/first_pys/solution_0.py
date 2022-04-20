

from collections import defaultdict

def main():
    # Get the string and query counts
    n, q = map(int, input().split())

    # Get the string
    s = input()

    # Get the queries
    queries = [list(map(int, input().split())) for _ in range(q)]

    # Create a dictionary to store the number of ACs in each substring
    ac_count = defaultdict(int)

    # Loop through the string
    for i in range(n-1):
        # If the current 2 characters are AC, increase the count
        if s[i:i+2] == 'AC':
            ac_count[i+1] += 1

    # Create a prefix sum array
    prefix_sums = [0]
    for i in range(1, n):
        prefix_sums.append(prefix_sums[i-1] + ac_count[i])

    # Loop through the queries
    for query in queries:
        # Get the start and end index
        l, r = query[0]-1, query[1]-1

        # Print the answer
        print(prefix_sums[r] - prefix_sums[l])

if __name__ == "__main__":
    main()