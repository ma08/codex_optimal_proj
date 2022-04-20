

def main():
    l = []
    n = int(input())
    for i in range(n):
        string = input()
        string = list(string)
        string.sort()
        if len(string) == 1:
            l.append("Yes")
        elif len(string) > 1:
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    l.append("No")
                    break
                elif ord(string[i]) + 1 == ord(string[i + 1]):
                    if i == len(string) - 2:
                        l.append("Yes")
                else:
                    l.append("No")
                    break
    for i in l:
        print(i)


if __name__ == "__main__":
    main()
