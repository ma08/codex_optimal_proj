

def stable_sort(files, attribute):
    return sorted(files, key=lambda x: x.split()[attribute], reverse=True)

def main():
    attributes = input().split()
    num_files = int(input())
    files = []
    for i in range(num_files):
        files.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for song in stable_sort(files, attributes.index(sort)):
            print(song)
        print()

if __name__ == "__main__":
    main()
