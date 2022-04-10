
def find_res(n, s, t):
    if s == t:
        return 'YES'
    elif s == 'ac' and t == 'bc':
        return 'YES'
    elif s == 'bc' and t == 'ac':
        return 'YES'
    elif s == 'ab' and t == 'cb':
        return 'YES'
    elif s == 'cb' and t == 'ab':
        return 'YES'
    return 'NO'

if __name__ == "__main__":
    n = int(input())
    s = input()
    t = input()
    res = find_res(n, s, t)
    print(res)
