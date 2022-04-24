

def main():
    # input the number of test cases
    n = int(input())

    # input each test case
    for i in range(n):
        # input
        s = input()
        t = input()

        # initialization
        count = 0

        # count the number of characters different between s and t
        for j in range(len(s)):
            if s[j] != t[j]:
                count += 1

        # output
        print(count)

if __name__ == '__main__':
    main()
