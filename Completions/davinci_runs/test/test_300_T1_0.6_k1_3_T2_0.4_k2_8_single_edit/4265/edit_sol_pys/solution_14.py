

def main():
    # input
    s = input()
    t = input()

    # count the number of characters different between s and t
    count = sum(s[i] != t[i] for i in range(len(s)))

    # output
    print(count)

if __name__ == '__main__':
    main()
