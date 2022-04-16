

# TODO: implement using a Trie instead of a hashmap (or not)


def main():
    s = input()
    q = int(input())

    d = {}
    for i, char in enumerate(s):
        if char not in d:
            d[char] = []
        d[char].append(i)

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            if query[2] not in d:
                d[query[2]] = []
            d[query[2]].append(int(query[1]) - 1)
        elif query[0] == '2':
            count = 0
            for char in d:
                if len(d[char]) > 0:
                    i, j = 0, len(d[char]) - 1
                    while i <= j:
                        mid = (i + j) // 2
                        if d[char][mid] < int(query[1]) - 1:
                            i = mid + 1
                        else:
                            j = mid - 1
                    if i < len(d[char]) and d[char][i] < int(query[2]):
                        count += 1
            print(count)


if __name__ == '__main__':
    main()
