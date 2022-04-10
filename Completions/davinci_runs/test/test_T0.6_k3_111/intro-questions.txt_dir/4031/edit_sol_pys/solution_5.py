
def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())

    # sort strings by length
    strings = sorted(strings, key=len)
    # sort strings by alphabet
    strings = sorted(strings)

    for i in range(1, n):
        if not strings[i].startswith(strings[i - 1]):
            print("NO")
            return
    print("YES")
    for s in strings:
        print(s)


main()
