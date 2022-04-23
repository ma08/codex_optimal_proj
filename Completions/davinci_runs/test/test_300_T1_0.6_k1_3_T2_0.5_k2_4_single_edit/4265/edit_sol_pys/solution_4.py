

def main():
    # input and initialization
    s = input()  # input
    t = input()  # input
    count = 0  # initialization

    # count the number of characters different between s and t, and store it in count
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    # output
    print(count)

if __name__ == '__main__':
    main()
