

def solve(n, b, a, s):
    i = 0
    b_charge = b
    a_charge = a
    max_dist = 0
    while i < n:
        if a_charge == 0 and s[i] == 1:
            a_charge += 1
            i += 1
        elif b_charge == 0 and s[i] == 0:
            b_charge += 1
            i += 1
        elif a_charge > 0 and s[i] == 0:
            a_charge -= 1
            i += 1
        elif b_charge > 0 and s[i] == 1:
            b_charge -= 1
            i += 1
        else:
            break
        max_dist += 1
    return max_dist

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(solve(n, b, a, s))
