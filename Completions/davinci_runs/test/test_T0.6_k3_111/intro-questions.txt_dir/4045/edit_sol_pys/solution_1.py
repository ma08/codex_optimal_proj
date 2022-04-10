

def find_res(n, s, t):
    if n % 2 == 0:
        if s == 'ac' and t == 'ac':
            return 'abc' * n
        elif s == 'cb' and t == 'cb':
            return 'abc' * n
        elif s == 'ab' and t == 'ab':
            return 'abc' * n
        elif s == 'bc' and t == 'bc':
            return 'abc' * n
        elif s == 'ac' and t == 'cb':
            return 'bac' * n
        elif s == 'ac' and t == 'ab':
            return 'cab' * n
        elif s == 'ac' and t == 'bc':
            return 'abc' * n
        elif s == 'cb' and t == 'ac':
            return 'abc' * n
        elif s == 'cb' and t == 'ab':
            return 'bac' * n
        elif s == 'cb' and t == 'bc':
            return 'cab' * n
        elif s == 'ab' and t == 'ac':
            return 'abc' * n
        elif s == 'ab' and t == 'cb':
            return 'abc' * n
        elif s == 'ab' and t == 'bc':
            return 'bac' * n
        elif s == 'bc' and t == 'ac':
            return 'cab' * n
        elif s == 'bc' and t == 'cb':
            return 'abc' * n
        elif s == 'bc' and t == 'ab':
            return 'abc' * n
        else:
            return 'NO'
    return 'NO'

if __name__ == "__main__":
    n = int(input())
    s = input()
    t = input()
    res = find_res(n, s, t)
    print(res)
