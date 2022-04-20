

def main():
    n = int(input())
    for i in range(n):
        string = input()
        if len(string) < 3:
            print("Dynamic")
        else:
            string = list(string)
            string.sort()
            if len(string) == 1:
                print("Dynamic")
            elif len(string) > 1:
                for i in range(len(string) - 1):
                    if string[i] == string[i + 1]:
                        print("Not")
                        break
                    elif ord(string[i]) + 1 == ord(string[i + 1]):
                        if i == len(string) - 2:
                            print("Dynamic")
                    else:
                        print("Not")
                        break


if __name__ == "__main__":
    main()
