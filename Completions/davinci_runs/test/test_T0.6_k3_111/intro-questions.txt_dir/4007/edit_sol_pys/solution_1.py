

def solve(friends):
    friends_dict = {}
    for i, j in enumerate(friends):
        if j == 0:
            friends_dict[i+1] = []
        else:
            friends_dict[j].append(i+1)
    res = list(friends)
    while len(friends_dict) > 0:
        key, val = friends_dict.popitem()
        if len(val) == 0:
            for k, v in friends_dict.items():
                if len(v) == 0:
                    continue
                res[k-1] = key
                val.append(k)
                break
        elif len(val) == 1:
            res[val[0]-1] = key
        else:
            for v in val:
                friends_dict[v].append(key)
    return res


def main():
    n = int(input())
    friends = [int(x) for x in input().split()]
    assert len(friends) == n
    res = solve(friends)
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
