

def answer(a):
    m = {}  # dictionary
    for i in range(len(a)):
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    max_len = max(m.values())
    count = 1
    for i in m.values():
        count *= (i + 1)
    count -= 1
    return count % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(a))
