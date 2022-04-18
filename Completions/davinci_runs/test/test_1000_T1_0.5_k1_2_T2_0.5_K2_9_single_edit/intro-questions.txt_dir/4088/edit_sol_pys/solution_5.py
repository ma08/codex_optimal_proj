

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        s = int(input())
        m = int(input())
        b = input().split()

        # create a dictionary for the mappings
        mapping = {}
        for j in range(len(s)):
            mapping[s[j]] = b[j]

        # create the result string
        res = ''
        for j in range(len(b)):
            res += mapping[b[j]]

        # print the result
        print(res)

if __name__ == "__main__":
    main()
