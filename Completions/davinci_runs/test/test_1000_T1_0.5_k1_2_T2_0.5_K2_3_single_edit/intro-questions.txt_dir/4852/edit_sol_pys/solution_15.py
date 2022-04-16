

def dpg(s):
    if '+' not in s:
        return int(s)
    else:
        count = 0
        for i in range(len(s)):
            if s[i] == '+':
                count += dpg(s[:i]) * dpg(s[i+1:])
        return count

print(dpg(input()))
