

def main():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string: "))
    for string in strings:
        string = list(string)
        string.sort()
        if len(string) == 1:
            print("YES")
        elif len(string) > 1:
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    print("NO")
                    break
                elif ord(string[i]) + 1 == ord(string[i + 1]):
                    if i == len(string) - 2:
                        print("YES")
                else:
                    print("NO")
                    break


if __name__ == "__main__":
    main()
