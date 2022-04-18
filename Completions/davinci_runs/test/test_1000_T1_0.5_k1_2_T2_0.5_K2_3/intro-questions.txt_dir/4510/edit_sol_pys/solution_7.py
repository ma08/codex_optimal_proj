
def main():
    n, k = [int(x) for x in input().split()] # n - number of people, k - maximum number of people to invite
    ids = [int(x) for x in input().split()] # ids of people that come to the party
    ids_to_count = {}
    for i in range(n):
        if ids[i] not in ids_to_count: # if the person is not in the list of people to invite
            if len(ids_to_count) == k:
                remove_id = min(ids_to_count.values()) # find the person with the least number of invites
                del ids_to_count[remove_id] # remove the person with the least number of invites
            ids_to_count[ids[i]] = 0
        else: # if the person is in the list of people to invite
            ids_to_count[ids[i]] += 1
        for id_ in ids_to_count: # increase the number of invites for all the people in the list
            if id_ != ids[i]:
                ids_to_count[id_] += 1
    print(len(ids_to_count))
    for id_ in ids_to_count:
        print(id_, end=' ')

if __name__ == "__main__":
    main()
