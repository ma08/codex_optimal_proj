
a = list(map(int, input().split())) # считывает построчно числа и записывает их в список
if sum(a) >= 22:
    print('bust')
else:
    print('win')
