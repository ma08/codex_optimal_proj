

def main():
    n = int(input())
    for i in range(n):
        string = input()
        string = list(string)
        string.sort()
        if len(string) == 1:
            print("Yes")
        else:
            if len(string) > 1:
                for i in range(len(string) - 1):
                    if string[i] == string[i + 1]:
                        print("No")
                        break
                    elif ord(string[i]) + 1 == ord(string[i + 1]):
                        if i == len(string) - 2:
                            print("Yes")
                    else:
                        print("No")
                        break
                else:
                    pass


if __name__ == "__main__":
    main()
