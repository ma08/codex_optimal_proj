
def main():
    n, k = [int(x) for x in input().split()]
    ids = [int(x) for x in input().split()]
    ids_to_count = {}
    for i in range(n):
        if ids[i] not in ids_to_count:
            if len(ids_to_count) == k:
                remove_id = min(ids_to_count.values())
                del ids_to_count[remove_id]
            ids_to_count[ids[i]] = 0
        else:
            ids_to_count[ids[i]] += 1
        for id_ in ids_to_count:
            if id_ != ids[i]:
                ids_to_count[id_] += 1
    print(len(ids_to_count))
    for id_ in ids_to_count:
        print(id_, end=' ')

if __name__ == "__main__":
    main()
