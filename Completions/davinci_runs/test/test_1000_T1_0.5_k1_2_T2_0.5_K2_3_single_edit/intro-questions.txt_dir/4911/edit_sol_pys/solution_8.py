

def stable_sort(songs, attribute, reverse=False):
    return sorted(songs, key=lambda x: x.split()[attribute])

def main():
    attributes = input().split()
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_songs):
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for song in stable_sort(songs, attributes.index(sort), reverse=False):
            print(song)
        print()

if __name__ == "__main__":
    main()
