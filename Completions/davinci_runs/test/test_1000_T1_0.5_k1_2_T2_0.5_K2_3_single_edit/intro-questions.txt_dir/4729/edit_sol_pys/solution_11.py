

def check_password(p, m):
    p = list(p)
    for i in range(len(p)):
        try:
            index = m.index(p[i])
        except ValueError:
            return "FAIL"
        m = m[index+1:]
    return "PASS"

print(check_password(input(), input()))
