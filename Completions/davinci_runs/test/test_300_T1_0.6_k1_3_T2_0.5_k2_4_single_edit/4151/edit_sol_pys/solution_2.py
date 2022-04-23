import math

def answer(a):
    m = {}
    for i in range(len(a)):
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    # print(m)
    # print(m.items())
    max_len = max(m.values())
    return math.factorial(max_len)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(a))
