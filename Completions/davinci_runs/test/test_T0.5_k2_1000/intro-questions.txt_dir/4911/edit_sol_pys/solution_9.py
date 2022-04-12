

def stable_sort(songs, attribute_index):
    return sorted(songs, key=lambda x: x[attribute_index])

def main():
    attributes = list(map(str, input().split()))
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(list(map(str, input().split())))
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(str(input()))
    for sort in sorts:
        for song in stable_sort(songs, attributes.index(sort) + 1):
            print(' '.join(song))
        print()

if __name__ == "__main__":
    main()
