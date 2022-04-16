

x = list(map(int, input().split()))

def next_permutation(a):
    for i in range(len(a)-1, 0, -1):
        if a[i-1] < a[i]:
            j = len(a)-1
            while a[j] < a[i-1]:
                j -= 1
            a[i-1], a[j] = a[j], a[i-1]
            a[i:] = a[len(a)-1: i-1: -1]
            return True
    return False

if next_permutation(list(x)):
    print(''.join(list(x)))
else:
    print(0)
