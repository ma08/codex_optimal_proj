
import sys


def main():
    n = int(sys.stdin.readline())  # number of strings
    strings = []
    for i in range(n):  # read all strings
        strings.append(sys.stdin.readline().strip())

    strings.sort(key=len, reverse=True)

    ok = True
    for i in range(n):
        for j in range(i):
            if strings[i] not in strings[j]:
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
