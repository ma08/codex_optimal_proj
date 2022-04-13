

villagers = int(input())  # количество деревенщин
nights = int(input())  # количество ночей
bard = 1  # бард
nights_songs = []  # список песен по ночям
for i in range(nights):  # ввод песен по ночям
    nights_songs.append(input().split()[1:])

songs = set()  # список песен барда и всех деревенщин
for i in range(nights):  # поиск песен барда и всех деревенщин
    if bard in nights_songs[i]:  # если бард поёт в ночь i
        songs.add(i)  # добавляем ночь i в список песен барда и всех деревенщин
    else:
        for j in range(nights):  # если бард не поёт в ночь i
            if i != j and set(nights_songs[i]).intersection(set(nights_songs[j])) != set():  # если в ночи i и j поёт хотя бы один деревенщина
                songs.add(i)  # добавляем ночь i в список песен барда и всех деревенщин
                songs.add(j)  # добавляем ночь j в список песен барда и всех деревенщин

for i in range(1, villagers+1): # поиск деревенщины, которая не поёт
    for j in range(nights): # перебор ночей
        if i in nights_songs[j] and j not in songs: # если деревенщина поёт в ночь j и ночь j не в списке песен барда и всех деревенщин
            break # переходим к следующей деревенщине
    else:
        print(i) # выводим деревенщину, которая не поёт
