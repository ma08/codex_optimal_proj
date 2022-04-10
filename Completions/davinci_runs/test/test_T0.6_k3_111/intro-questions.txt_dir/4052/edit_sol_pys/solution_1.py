

def main():
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    t = input()
    """
    n = 6
    s = "abcdef"
    t = "abdfec"
    s = "abcd"
    t = "accd"

    result = swapLexOrder(s, t, n)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()


def swapLexOrder(s, t, n):
    pass


if __name__ == '__main__':
    main()
