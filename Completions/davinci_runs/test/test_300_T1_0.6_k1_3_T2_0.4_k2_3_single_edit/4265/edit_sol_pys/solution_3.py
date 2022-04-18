

def main():
    # open file
    f = open('file.txt', 'r')

    # read file
    s = f.read()

    # count the number of characters different between s and t
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    # output
    print(count)

if __name__ == '__main__':
    main()
