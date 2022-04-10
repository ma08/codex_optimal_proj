
def solve(friend):
    friend_dict = {}
    for i, j in enumerate(friend):
        if j == 0:
            friend_dict[i+1] = []
        else:
            friend_dict[j].append(i+1)
    res = list(friend)
    while len(friend_dict) > 0:
        key, val = friend_dict.popitem()
        if len(val) == 0:
            for k, v in friend_dict.items():
                if len(v) == 0:
                    continue
                res[k-1] = key
                val.append(k)
                break
        elif len(val) == 1:
            res[val[0]-1] = key
        else:
            for v in val:
                friend_dict[v].append(key)
    return res


def main():
    n = int(input())
    friend = [int(x) for x in input().split()]
    assert len(friend) == n
    res = solve(friend)
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
