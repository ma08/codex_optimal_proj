

import sys

N, A, B, C = map(int, sys.stdin.readline().strip().split())
l_i = [int(sys.stdin.readline().strip()) for _ in range(N)]

# MP = (A-a)+(B-b)+(C-c)+10*(n-3)
# a = A-MP+(B-b)+(C-c)+10*(n-3)
# b = B-MP+(A-a)+(C-c)+10*(n-3)
# c = C-MP+(A-a)+(B-b)+10*(n-3)

def calc_mp(n, a, b, c):
    return (A-a)+(B-b)+(C-c)+10*(n-3)

def calc_a(mp, b, c):
    return A-mp+(B-b)+(C-c)+10*(N-3)

def calc_b(mp, a, c):
    return B-mp+(A-a)+(C-c)+10*(N-3)

def calc_c(mp, a, b):
    return C-mp+(A-a)+(B-b)+10*(N-3)

def is_valid(mp, a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    for l in l_i:
        if l == a:
            a = 0
        elif l == b:
            b = 0
        elif l == c:
            c = 0
    return True if a+b+c == 0 else False

def main():
    mp = None
    for a in range(1, A+1):
        for b in range(a+1, B+1):
            for c in range(b+1, C+1):
                if is_valid(calc_mp(N, a, b, c), a, b, c):
                    mp = calc_mp(N, a, b, c)
                    break
            else:
                continue
            break
        else:
            continue
        break
    print(mp)

if __name__ == "__main__":
    main()