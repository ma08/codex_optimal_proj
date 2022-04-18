
from collections import Counter

def is_all_same(a):
    return a[0] == a[1] == a[2] == a[3]

def max_product(a):
    if is_all_same(a):
        return a[0]**2
    else:
        return max(a[0]*a[1], a[2]*a[3])

def max_product_with_one_pair(a):
    c = Counter(a)
    # print(c)
    for i in range(4):
        if c[a[i]] == 2:
            for j in range(4):
                if j != i:
                    return a[i]**2 * a[j]

def max_product_with_two_pair(a):
    c = Counter(a)
    # print(c)
    for i in range(4):
        if c[a[i]] == 2:
            for j in range(4):
                if j != i and c[a[j]] == 2:
                    return a[i]**2 * a[j]**2

def max_product_with_three_pair(a):
    c = Counter(a)
    # print(c)
    for i in range(4):
        if c[a[i]] == 3:
            for j in range(4):
                if j != i and c[a[j]] == 2:
                    return a[i]**3 * a[j]**2


def main():
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    print(max(max_product(a), max_product_with_one_pair(a), max_product_with_two_pair(a), max_product_with_three_pair(a)))

if __name__ == "__main__":
    main()
