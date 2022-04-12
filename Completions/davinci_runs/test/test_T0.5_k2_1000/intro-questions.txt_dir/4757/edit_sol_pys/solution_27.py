
villagers = int(input())
nights = int(input())
nights_songs = []
for i in range(nights):
    nights_songs.append(input().split()[1:])

songs = set()
for i in range(nights):
    for j in range(nights):
        if i != j and set(nights_songs[i]).intersection(set(nights_songs[j])) != set():
            songs.add(i)
            songs.add(j)

for i in range(villagers):
    for j in range(nights):
        if i in nights_songs[j] and j not in songs:
            break
    else:
        print(i)
