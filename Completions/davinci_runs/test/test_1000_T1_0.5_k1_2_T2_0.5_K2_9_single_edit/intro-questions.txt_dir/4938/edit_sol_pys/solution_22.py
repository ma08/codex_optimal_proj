

def main():
    # read in the input
    n = int(input())
    # loop through the input
    for i in range(n):
        # read in the number of rows
        rows = int(input())
        # loop through the rows
        for j in range(rows):
            # read in the number of columns
            cols = int(input())
            # loop through the columns
            for k in range(cols):
                # read in the entry
                entry = int(input())
                # print the entry
                print(entry)

if __name__ == "__main__":
    main()
