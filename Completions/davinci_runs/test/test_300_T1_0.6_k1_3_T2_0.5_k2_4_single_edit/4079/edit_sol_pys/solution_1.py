

def main():
    n = int(input())
    for i in range(n):
        string = input()
        string = sorted(string)
        if len(string) == 1:
            print("Yes")
        elif len(string) > 1:
            for j in range(len(string) - 1):
                if string[j] == string[j + 1]:
                    print("No")
                    break
                elif ord(string[j]) + 1 == ord(string[j + 1]):
                    if j == len(string) - 2:
                        print("Yes")
                else:
                    print("No")
                    break


if __name__ == "__main__":
    main()
