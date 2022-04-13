

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        s = input()
        n = int(input())
        b = list(map(int, input().split()))

        # create a dictionary for the mappings
        mapping = {}
        for j in range(n):
            mapping[b[j] - 1] = j

        # create the result string
        res = ''
        for j in range(n):
            res += chr(ord('a') + mapping[j])

        # print the result
        print(res)

if __name__ == "__main__":
    main()
