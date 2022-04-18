

def main():
    n = int(input())
    test = input()
    if len(test) != len(set(test)):
        print('No')
    elif ord(test[-1]) - ord(test[0]) != len(test)-1:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
