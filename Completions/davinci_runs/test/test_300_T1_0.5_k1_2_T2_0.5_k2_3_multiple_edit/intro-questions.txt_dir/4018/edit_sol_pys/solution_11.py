

def main():
    n, k = map(int, input().split())
    s = input()

    s = [c for c in s]
    s.sort(reverse=True)
    s = "".join(s)

    curr = ""
    res = [curr]
    for c in s:
        if len(curr) < k:
            curr += c
        else:
            curr = c
            res.append(curr)

    print(len(res))
    print(" ".join(map(str, res)))

main()
