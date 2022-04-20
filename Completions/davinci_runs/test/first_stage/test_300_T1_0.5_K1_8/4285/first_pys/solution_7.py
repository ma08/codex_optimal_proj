


#Solution

def find_subsequences_abc(n, s):
    MOD = 10**9 + 7
    cnt_a, cnt_b, cnt_c = 0, 0, 0
    for c in s:
        if c == 'a':
            cnt_a = (cnt_a + 1) % MOD
        elif c == 'b':
            cnt_b = (cnt_b + cnt_a) % MOD
        elif c == 'c':
            cnt_c = (cnt_c + cnt_b) % MOD
    return cnt_c


n = int(input())
s = input()
print(find_subsequences_abc(n, s))