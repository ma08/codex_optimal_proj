

def main():
    n, k = [int(x) for x in input().split()]
    ids = [int(x) for x in input().split()] #list of input ids
    ids_to_pos = {}
    for i in range(n):
        if ids[i] not in ids_to_pos: #if the element is not in the dictionary
            if len(ids_to_pos) == k: #if the dictionary is full
                remove_id = min(ids_to_pos.values()) #find the element with the least number of occurences
                del ids_to_pos[remove_id] #delete it
            ids_to_pos[ids[i]] = 0 #add the new element
        else:
            ids_to_pos[ids[i]] += 1 #if the element is already in the dictionary, increase its value
        for id_ in ids_to_pos:
            if id_ != ids[i]:
                ids_to_pos[id_] += 1
    print(len(ids_to_pos))
    for id_ in ids_to_pos:
        print(id_, end=' ')

if __name__ == "__main__":
    main()
