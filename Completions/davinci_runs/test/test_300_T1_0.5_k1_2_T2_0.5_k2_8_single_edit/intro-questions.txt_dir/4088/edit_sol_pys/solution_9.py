

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        n = int(input())
        a = list(map(int, input().split()))

        # create a dictionary for the mappings
        mapping = {}
        for j in range(len(a)):
            mapping[a[j]] = j

        # create the result string
        res = []
        for j in range(len(a)):
            res.append(mapping[j])

        # print the result
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
