

def dpg(string, d):
    if '+' not in string:
        return d
    else:
        count = 0
        for i in range(len(string)):
            if string[i] == '+':
                count += dpg(string[:i], d+1) * dpg(string[i+1:], d+1)
        return count

print(dpg(input()))
