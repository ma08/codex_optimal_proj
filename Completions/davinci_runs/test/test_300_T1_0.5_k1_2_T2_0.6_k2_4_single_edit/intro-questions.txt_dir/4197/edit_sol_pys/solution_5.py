

# N = int(input())
# A = [int(i) for i in input().split()]

# for i in range(N):
#     print(A.index(i+1)+1, end=' ')


n, m = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

b = [int(i) for i in input().split()]

answer = 0


def are_equal(a, b):
    a = [i for i in a]
    b = [i for i in b]
    return a == b


def permute(a, l, r):
    if l == r:
        print(a)
        if are_equal(a, b):
            global answer
            answer = 1
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


permute(a, 0, n-1)
print(answer)
