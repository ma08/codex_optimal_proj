
def stable_sort(songs, attribute):
    return sorted(songs, key=lambda x: x[attribute])

def main():
    attributes = input().split()
    num_songs = int(input())
    songs = [[] for i in range(num_songs)]
    for i in range(num_songs):
        songs[i] = input().split()
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
    for i in range(num_songs):
        for j in range(len(attributes)):
            if attributes[j] == 'artist':
                songs[i][j] = songs[i][j].lower()
            else:
                songs[i][j] = int(songs[i][j])
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for song in stable_sort(songs, attributes.index(sort)):
            print(' '.join(song))
        print()

if __name__ == "__main__":
    main()
