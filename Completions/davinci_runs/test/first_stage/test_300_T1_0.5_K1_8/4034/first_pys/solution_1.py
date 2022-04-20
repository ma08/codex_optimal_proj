

n = int(input())
s = input()

def is_sorted(s):
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def is_sorted_after_swap(s):
    i = 0
    while i < len(s)-1:
        if s[i] > s[i+1]:
            break
        i += 1
    if i == len(s)-1:
        return True
    else:
        j = i+1
        while j < len(s)-1:
            if s[j] > s[j+1]:
                return False
            j += 1
        return True

def get_color(s, i):
    if i == 0:
        return '0' if s[i] <= s[i+1] else '1'
    if i == len(s)-1:
        return '0' if s[i] >= s[i-1] else '1'
    return '0' if s[i] >= s[i-1] and s[i] <= s[i+1] else '1'

if is_sorted(s):
    print('YES')
    print('0' * n)
elif is_sorted_after_swap(s):
    print('YES')
    print(''.join(get_color(s, i) for i in range(n)))
else:
    print('NO')