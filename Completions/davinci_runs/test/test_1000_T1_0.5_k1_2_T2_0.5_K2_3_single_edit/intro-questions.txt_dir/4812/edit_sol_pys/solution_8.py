

from sys import stdin

word = stdin.readline().strip()
endings = []
for i in range(int(stdin.readline().strip())):  # введение окончаний
    endings.append(stdin.readline().strip().split())  # окончания в виде списка
for i in range(int(stdin.readline().strip())):
    phrase = stdin.readline().strip().split()
    if len(phrase) == 2:  # если 2 слова
        if phrase[1] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))]:  # если окончание в списке окончаний
            print("YES")
        else:
            print("NO")
    else:  # если 3 слова
        if phrase[1] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))] and phrase[2] in endings[endings.index(list(filter(lambda x: word.endswith(x), endings)))]:  # если окончания в списке окончаний
            print("YES")
        else:
            print("NO")
