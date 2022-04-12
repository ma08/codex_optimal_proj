

def stable_sort(songs, attribute_index):
    return sorted(songs, key=lambda x: x.split('|')[attribute_index])

def main():
    attributes = input().split('|')
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(input())
    for sort in sorts:
        print('|'.join(attributes))
        for song in stable_sort(songs, attributes.index(sort)):
            print(song)
        print()

if __name__ == "__main__":
    main()
