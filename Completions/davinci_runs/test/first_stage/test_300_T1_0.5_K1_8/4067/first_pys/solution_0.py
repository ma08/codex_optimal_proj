

N = int(input())
S = input()

def solve():
    n0 = S.count('0')
    n1 = S.count('1')
    n2 = S.count('2')
    if n0 == n1 == n2:
        return S

    n = N // 3
    s = list(S)
    for i in range(N):
        if s[i] == '0':
            if n0 > n:
                s[i] = '2'
                n0 -= 1
                n2 += 1
        elif s[i] == '1':
            if n1 > n:
                s[i] = '0'
                n1 -= 1
                n0 += 1
        else:
            if n2 > n:
                s[i] = '1'
                n2 -= 1
                n1 += 1

    return ''.join(s)

print(solve())