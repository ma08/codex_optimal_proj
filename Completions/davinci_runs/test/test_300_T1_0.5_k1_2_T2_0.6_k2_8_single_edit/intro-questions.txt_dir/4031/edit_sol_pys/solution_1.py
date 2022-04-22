

from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    strings = []
    for i in range(n):
        strings.append(stdin.readline().strip())

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
        stdout.write("YES\n")
        for s in strings:
            stdout.write(s + "\n")
    else:
        stdout.write("NO")


if __name__ == "__main__":
    main()
