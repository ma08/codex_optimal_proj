

def main():
    string = input()
    if len(string) != len(set(string)):
        print('No')
    elif ord(string[-1]) - ord(string[0]) != len(string)-1:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
