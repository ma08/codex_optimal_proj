

def main():
    n, k = [int(x) for x in input().split()]
    ids = [int(x) for x in input().split()]
    ids_to_pos = []
    for i in range(n):
        if ids[i] not in ids_to_pos and len(ids_to_pos) < k:
            ids_to_pos.append(ids[i])
    for i in range(n):
        if ids[i] not in ids_to_pos:
            remove_id = ids_to_pos[0]
            ids_to_pos.pop(0)
            ids_to_pos.append(ids[i])
    print(len(ids_to_pos))
    for id_ in ids_to_pos:
        print(id_, end=' ')

if __name__ == "__main__":
    main()
