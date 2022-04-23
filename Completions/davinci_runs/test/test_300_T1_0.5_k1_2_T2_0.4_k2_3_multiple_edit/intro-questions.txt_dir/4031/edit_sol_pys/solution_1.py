
import sys


def main():
    n = int(sys.stdin.readline())
    strings = []  # list of strings
    for i in range(n):
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)  # sort by length

    ok = True  # check if all strings are substrings of previous strings
    for i in range(n):
        for j in range(i):  # check if strings[i] is substring of strings[j] (j < i)
            if strings[i] not in strings[j]:  # if strings[i] is not substring of strings[j] (j < i)
                ok = False
                break
        if not ok:
            break

    if ok:  # if all strings are substrings of previous strings
        print("YES")
        for s in strings:
            print(s)
    else:  # if not
        print("NO")


if __name__ == "__main__":
    main()
