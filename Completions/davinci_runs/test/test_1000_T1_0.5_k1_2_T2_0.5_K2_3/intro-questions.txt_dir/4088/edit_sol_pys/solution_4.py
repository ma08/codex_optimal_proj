

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        s = input()
        m = int(input())
        b = list(map(int, input().split()))

        # create a dictionary for the mappings
        mapping = {}
        for j in range(len(b)):
            mapping[b[j]] = j

        # create the result string, split the string into letters
        # use the mapping to create the new string
        res = []
        for j in s:
            res.append(chr(ord('a') + mapping[j]))

        # print the result
        print(''.join(res))

if __name__ == "__main__":
    main()
