


def main():
    n = int(input())
    strings = []
    for x in range(n):
        strings.append(input())
    strings.sort(key=lambda s: len(s))

    for i in range(n):
        for j in range(i):
            if strings[i].find(strings[j]) != 0:
                print("NO")
                return
    print("YES")
    for s in strings:
        print(s)


if __name__ == "__main__":
    main()