

def answer(a):
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    # print(m)
    # print(m.items())
    max_len = max(m.values())
    count = 1
    for i in m.values():
        count *= (i + 1)
    # print(count)
    count -= 1
    return count % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(a))
