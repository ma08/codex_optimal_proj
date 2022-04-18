

def stable_sort(songs, attribute):
    return sorted(songs, key=lambda x: x.split()[attribute], reverse=True)

def main():
    attributes = input().split()[::-1]
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for song in stable_sort(songs, len(attributes) - attributes.index(sort) - 1):
            print(song)
        print()

if __name__ == "__main__":
    main()
