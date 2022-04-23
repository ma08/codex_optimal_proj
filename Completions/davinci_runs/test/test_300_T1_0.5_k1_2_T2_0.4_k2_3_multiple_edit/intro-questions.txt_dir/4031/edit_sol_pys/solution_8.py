
import sys


def main():
    n = int(sys.stdin.readline())
    strings = []  # array of strings
    for i in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)  # sort by length

    ok = True  # check if all strings are substrings of previous
    for i in range(n):
        for j in range(i):  # check if strings[i] is substring of strings[j]
            if strings[i] not in strings[j]:  # if strings[i] is not substring of strings[j]
                ok = False
                break
        if not ok:
            break

    if ok:  # if all strings are substrings of previous
        print("YES")
        for string in strings:
            print(string)
    else:  # if not
        print("NO")


if __name__ == "__main__":
    main()
