

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        a = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))[:m]

        # create a dictionary for the mappings
        mapping = {}
        for j in range(m):
            mapping[b[j]] = j + 1

        # create the result string
        res = ''
        for j in range(len(a)):
            res += str(mapping[a[j]]) + ' '

        # print the result
        print(res)

if __name__ == "__main__":
    main()
