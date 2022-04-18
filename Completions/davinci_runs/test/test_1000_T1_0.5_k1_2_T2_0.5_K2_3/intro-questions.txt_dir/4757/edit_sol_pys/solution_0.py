

villagers = int(input())
nights = int(input())
bard = int(input())
nights_songs = []
for _ in range(nights):
    nights_songs.append(input().split()[1:])

songs = set()
for i in range(nights-1):
    if bard in nights_songs[i]:
        songs.add(i)
    else:
        for j in range(i+1, nights):
            if i != j and set(nights_songs[i]).intersection(set(nights_songs[j])) != set():
                songs.add(i)
                songs.add(j)

for i in range(1, villagers+1):
    if bard == i:
        continue
    for j in range(nights):
        if i in nights_songs[j] and j not in songs:
            break
    else:
        print(i)
