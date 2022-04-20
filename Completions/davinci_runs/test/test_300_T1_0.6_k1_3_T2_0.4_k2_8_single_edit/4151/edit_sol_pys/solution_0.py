
def answer(a):
    n = len(a)
    m = {}
    for i in range(n):
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    # print(m)
    # print(m.items())
    max_len = max(m.values())
    count = 1
    for i in m.values():
        count *= (i + 1)
    # print(count)
    count -= 1
    return count % 998244353

def answer(a):
    m = {}
    n = len(a)
    for i in range(n):
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    # print(m)
    # print(m.items())
    max_len = max(m.values())
    count = 1
    for i in m.values():
        count *= (i + 1)
    # print(count)
    count -= 1
    return count

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(a))
