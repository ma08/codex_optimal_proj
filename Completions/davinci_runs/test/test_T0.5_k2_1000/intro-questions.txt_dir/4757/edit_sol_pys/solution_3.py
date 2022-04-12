
villagers = int(input())
nights = int(input())
bard = 0
nights_songs = []
for i in range(nights):
    nights_songs.append(set(input().split()[1:]))

songs_list = []
for i in range(nights - 1):
    for j in range(i + 1, nights):
        if nights_songs[i].intersection(nights_songs[j]) != set():
            songs_list.append(set([i, j]))

songs = set(range(nights))
for song in songs_list:
    songs = songs.difference(song)

for i in range(villagers):
    if i not in nights_songs[bard] and i != bard:
        for j in range(nights):
            if i in nights_songs[j] and j not in songs:
                break
        else:
            print(i)
