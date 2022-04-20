

def get_boots_pair(n, l, r):
    ll = [0] * 26
    rr = [0] * 26
    for i in range(n):
        if l[i] != '?':
            ll[ord(l[i]) - ord('a')] += 1
        if r[i] != '?':
            rr[ord(r[i]) - ord('a')] += 1

    pairs = []
    for i in range(n):
        if l[i] != '?' and r[i] != '?':
            pairs.append([i, i])
            ll[ord(l[i]) - ord('a')] -= 1
            rr[ord(r[i]) - ord('a')] -= 1
        elif l[i] != '?':
            j = ord(l[i]) - ord('a')
            if rr[j] > 0:
                pairs.append([i, n - rr[j]])
                rr[j] -= 1
                ll[j] -= 1
        elif r[i] != '?':
            j = ord(r[i]) - ord('a')
            if ll[j] > 0:
                pairs.append([n - ll[j], i])
                rr[j] -= 1
                ll[j] -= 1
        else:
            for j in range(26):
                if ll[j] > 0 and rr[j] > 0:
                    pairs.append([n - ll[j], n - rr[j]])
                    rr[j] -= 1
                    ll[j] -= 1
                    break
    return pairs

if __name__ == '__main__':
    n = int(input())
    l = input()
    r = input()
    pairs = get_boots_pair(n, l, r)
    print(len(pairs))
    for p in pairs:
        print(p[0] + 1, p[1] + 1)