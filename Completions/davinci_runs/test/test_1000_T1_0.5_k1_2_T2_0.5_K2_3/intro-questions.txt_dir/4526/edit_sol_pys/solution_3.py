

def main():
    # Read number of test cases.
    t = int(input())

    # Iterate over test cases.
    for i in range(t):
        # Read length of array.
        n = int(input())
        # Read array.
        a = list(map(int, input().split()))

        # Find sum of consecutive elements.
        # and check if sum is in array.
        # If yes, increase counter.
        counter = 0
        for j in range(n):
            s = a[j]
            if s in a:
                counter += 1
            for k in range(j+1, n):
                s += a[k]
                if s in a:
                    counter += 1
                if s > n:
                    break

        # Print number of special elements.
        print(counter)

if __name__ == "__main__":
    main()
