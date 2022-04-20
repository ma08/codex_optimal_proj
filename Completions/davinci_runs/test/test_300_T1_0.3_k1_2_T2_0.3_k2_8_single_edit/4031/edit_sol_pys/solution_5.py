
#

def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())

    strings.sort(key=len)

    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            print("NO")
            return

    print("YES")
    for string in strings:
        print(string)


if __name__ == "__main__":
    main()
