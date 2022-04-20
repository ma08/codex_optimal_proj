
import sys


def main():
    n = int(sys.stdin.readline())
    strings = ['']
    for i in range(n):
        strings.append(sys.stdin.readline().strip())  # readline() returns a string with a trailing newline character

    strings.sort(key=len, reverse=True)  # sort by length

    ok = True
    for i in range(n):
        for j in range(i):
            if strings[i] not in strings[j]:  # check if a string is a substring of another
                ok = False
                break
        if not ok:
            break

    if ok:
        print("YES")
        for s in strings:
            print(s)
    else:
        print("NO")


if __name__ == "__main__":
    main()
