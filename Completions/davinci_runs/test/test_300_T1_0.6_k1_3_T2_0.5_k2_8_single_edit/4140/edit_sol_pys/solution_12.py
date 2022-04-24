


def main():
    s = input("Enter the string: ")
    count = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
