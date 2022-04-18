

from sys import stdin

def main():
    word = stdin.readline().strip()
    endings = []
    for i in range(int(stdin.readline().strip())):
        endings.append(stdin.readline().strip().split())
    for i in range(int(stdin.readline().strip())):
        phrase = stdin.readline().strip().split()
        if len(phrase) == 2:
            if phrase[1] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))]:
                print("YES")
            else:
                print("NO")
        else:
            if phrase[1] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))] and phrase[2] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))]:
                print("YES")
            else:
                print("NO")
main()
