

def main():
    # Read input number of test cases
    t = int(input())
    # Iterate through test cases
    for i in range(t):
        # Read input number of rows
        n = int(input())
        # Read input rows
        rows = []
        for j in range(n):
            row = input()
            rows.append(row)
        # Output solution
        print("Case #{}: {}".format(i + 1, solve(rows)))


def solve(rows):
    # Initialize dictionary to store number of times each color appears in each column
    column_counts = {}
    # Iterate through rows
    for row in rows:
        # Iterate through characters in row
        for i, char in enumerate(row):
            # If this is the first time seeing this color in this column, initialize count to 1
            if char not in column_counts:
                column_counts[char] = [0] * len(row)
                column_counts[char][i] = 1
            # If this color has been seen in this column before, increment count
            else:
                column_counts[char][i] += 1
    # Initialize string to store solution
    solution = ""
    # Iterate through columns
    for i in range(len(rows[0])):
        # Initialize variable to store number of times most common color appears in this column
        max_count = 0
        # Initialize variable to store most common color in this column
        max_color = None
        # Iterate through colors
        for color in column_counts:
            # If this color appears more times than any other color, update max_count and max_color
            if column_counts[color][i] > max_count:
                max_count = column_counts[color][i]
                max_color = color
        # Add most common color to solution
        solution += max_color
    # Return solution
    return solution


if __name__ == "__main__":
    main()
