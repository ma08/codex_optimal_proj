import sys

villagers = int(input())
sys.setrecursionlimit(10000000)
nights = int(input())
bard = 1
nights_songs = []
for i in range(nights):
    nights_songs.append(list(map(int, input().split()[1:])))

def find_songs(songs, i):
    if bard in nights_songs[i]:
        songs.append(i)
    for j in range(nights):
        if i != j and set(nights_songs[i]).intersection(set(nights_songs[j])) != set():
            songs.append(i)
            songs.append(j)
            find_songs(songs, j)
            break
    return songs

songs = find_songs([], 0)

for i in range(1, villagers+1):
    for j in range(nights):
        if i in nights_songs[j] and j not in songs:
            break
    else:
        print(i)
