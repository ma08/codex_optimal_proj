

    a = 0
def main():
    result = []
    n = int(input())
    for i in range(n):
        string = input()
        string = list(string)
        string.sort()
        if len(string) == 1:
            result.append("Yes")
        elif len(string) > 1:
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    result.append("No")
                    break
                elif ord(string[i]) + 1 == ord(string[i + 1]):
                    if i == len(string) - 2:
                        result.append("Yes")
                else:
                    result.append("No")
                    break
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
