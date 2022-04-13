

from sys import stdin, stdout


def main():
    word = stdin.readline().strip()
    endings = []
    for i in range(int(stdin.readline().strip())):
        endings.append(stdin.readline().strip().split())
    for i in range(int(stdin.readline().strip())):
        phrase = stdin.readline().strip().split()
        if len(phrase) == 2:
            if phrase[1] in list(filter(lambda x: word.endswith(x), endings)):
                stdout.write("YES\n")
            else:
                stdout.write("NO\n")
        else:
            if phrase[1] in list(filter(lambda x: word.endswith(x), endings)) and phrase[2] in list(filter(lambda x: word.endswith(x), endings)):
                stdout.write("YES\n")
            else:
                stdout.write("NO\n")


if __name__ == '__main__':
    main()
