

def main():
    # Read in number of test cases
    t = int(input())
    # Iterate through test cases
    for i in range(t):
        # Read in number of rows and columns
        n, m = map(int, input().split())
        # Read in rows
        rows = []
        for j in range(n):
            row = list(map(int, input().split()))
            rows.append(row)
        # Read in columns
        cols = []
        for j in range(m):
            col = list(map(int, input().split()))
            cols.append(col)
        # Print result
        print(valid(rows, cols))


def valid(rows, cols):
    """
    Returns whether the input is valid
    """
    # Iterate through rows
    for i in range(len(rows)):
        # Iterate through columns
        for j in range(len(cols)):
            # Check if columns and rows are equal
            if rows[i][j] != cols[j][i]:
                return "No"
    # If all checks passed, return "Yes"
    return "Yes"


if __name__ == "__main__":
    main()
