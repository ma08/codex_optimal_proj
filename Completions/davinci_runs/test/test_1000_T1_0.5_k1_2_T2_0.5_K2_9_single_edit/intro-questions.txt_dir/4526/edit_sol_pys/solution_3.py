

def main():
    # Read number of test cases
    t = int(input())

    # Iterate over test cases
    for i in range(t):
        # Read length of array
        n = int(input())
        # Read array
        a = list(map(int, input().split()))

        counter = 0
        for j in range(n):
            if a[j] in a[:j] + a[j+1:]:
                counter += 1 

        # Print number of special elements
        print(counter)

if __name__ == "__main__":
    main()
