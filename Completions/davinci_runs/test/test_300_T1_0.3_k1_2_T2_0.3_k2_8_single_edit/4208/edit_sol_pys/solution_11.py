

def check(l, r):
    if l == '?' or r == '?':
        return True
    elif l == r:
        return True
    else:
        return False

def main():
    n = int(input())
    l = input()
    r = input()
    res = 0
    pairs = []
    for i in range(n):
        if check(l[i], r[i]):
            res += 1
            pairs.append([i+1, i+1])
    for i in range(n):
        for j in range(n):
            if i != j and check(l[i], r[j]):
                res += 1
                pairs.append([i+1, j+1])
                break
    print(res)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    main()
