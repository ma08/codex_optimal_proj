

def stable_sort(lines, attribute_index):
    return sorted(lines, key=lambda x: x.split()[attribute_index])

def main():
    attributes = input().split()
    num_songs = int(input())
    lines = []
    for i in range(num_songs):
        lines.append(input())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(input())
    for sort in sorts:
        print(' '.join(attributes))
        for line in stable_sort(lines, attributes.index(sort)):
            print(line)
        print()

if __name__ == "__main__":
    main()
