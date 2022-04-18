

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        s = input()
        b = list(map(int, input().split()))

        # create a dictionary for the mappings
        mapping = {}
        for k in range(len(b)):
            mapping[k] = b[k]

        # create the result string
        res = ''
        for k in range(len(s)):
            res += chr(ord('a') + mapping[k])

        # print the result
        print(res)

if __name__ == "__main__":
    main()
