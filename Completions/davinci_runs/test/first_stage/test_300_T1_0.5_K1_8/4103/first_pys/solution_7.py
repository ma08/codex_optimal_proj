

def rob_battery_solar(n, b, a, s):
    i = 0
    charge = [b, a]
    while i < n:
        if s[i] == 1:
            if charge[0] > 0:
                charge[0] -= 1
                charge[1] += 1
                if charge[1] > a:
                    charge[1] -= 1
            elif charge[1] > 0:
                charge[1] -= 1
        else:
            if charge[0] > 0:
                charge[0] -= 1
            else:
                charge[1] -= 1
        i += 1
        if charge[0] < 0 or charge[1] < 0:
            break
    return i

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(rob_battery_solar(n, b, a, s))