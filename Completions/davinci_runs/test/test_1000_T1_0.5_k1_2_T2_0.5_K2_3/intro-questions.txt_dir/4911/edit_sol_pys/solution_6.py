

def stable_sort(lines, attribute):
    return sorted(lines, key=lambda x: x[attribute])

def main():
    attributes = input().split()
    attributes_index = {attributes[i]: i for i in range(len(attributes))}
    num_songs = int(input())
    lines = []
    for i in range(num_songs):
        lines.append(input().split())
    num_sorts = int(input())
    sorts = []
    for i in range(num_sorts):
        sorts.append(input().split())
    for sort in sorts:
        print(' '.join(attributes))
        for line in stable_sort(lines, attributes_index[sort]):
            print(' '.join(line))
        print()

if __name__ == "__main__":
    main()
