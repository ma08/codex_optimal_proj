

def main():
    # read the input
    s = input()
    m = int(input())
    b = list(map(int, input().split()))

    # create a dictionary for the mappings
    mapping = {}
    for i in range(len(b)):
        mapping[b[i]] = i

    # create the result string
    res = ''
    for i in range(len(s)):
        res += chr(ord('a') + mapping[i])

    # print the result
    print(res)

if __name__ == "__main__":
    main()
