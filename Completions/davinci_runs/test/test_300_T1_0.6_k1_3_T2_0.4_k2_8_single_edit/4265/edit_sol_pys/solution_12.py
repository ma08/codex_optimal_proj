

def main():
    # input:
    #   s: str
    #   t: str
    # output:
    #   the number of characters different between s and t: int
    s = input()  # str
    t = input()  # str

    # initialization
    count = 0

    # count the number of characters different between s and t
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    # output
    print(count)

if __name__ == '__main__':
    main()
