

def main():
    n = int(input())
    for i in range(n):
        test_string = input()
        if len(test_string) != len(set(test_string)):
            print('No')
        elif ord(test_string[-1]) - ord(test_string[0]) != len(test_string)-1:
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    main()
