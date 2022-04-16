

def stable_sort(songs, attribute, reverse=False):
    return sorted(songs, key=lambda x: x.split()[attribute], reverse=reverse)

def main():
    attributes = input().split()
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
    songs = stable_sort(songs, attributes.index('Year'))
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for song in stable_sort(songs, attributes.index(sort)):
            print(song)
        print()

if __name__ == "__main__":
    main()
