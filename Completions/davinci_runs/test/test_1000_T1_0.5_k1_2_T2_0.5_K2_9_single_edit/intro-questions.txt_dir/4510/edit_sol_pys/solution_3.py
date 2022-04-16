

def main():
    n, k = [int(x) for x in input().split()]
    ids = [int(x) for x in input().split()]
    ids_to_pos = {}
    for i in range(n):
        if ids[i] not in ids_to_pos:
            if len(ids_to_pos) == k:
                remove_id = min(ids_to_pos.values())
                del ids_to_pos[remove_id]
            ids_to_pos[ids[i]] = 0
        else:
            ids_to_pos[ids[i]] += 1
        for id_ in ids_to_pos:
            if id_ != ids[i]:
                ids_to_pos[id_] += 1
    print(len(ids_to_pos), end=' ')
    for id_ in ids_to_pos:
        print(id_, end=' ')

if __name__ == "__main__":
    main()
