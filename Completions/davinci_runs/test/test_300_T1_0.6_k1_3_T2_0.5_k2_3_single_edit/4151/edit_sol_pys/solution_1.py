

def answer(n, a):
    m = [0] * (n + 1)
    m[0] = 1
    for i in range(1, n + 1):
        for j in a:
            if i >= j:
                m[i] += m[i - j]
    return m[n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(a))
