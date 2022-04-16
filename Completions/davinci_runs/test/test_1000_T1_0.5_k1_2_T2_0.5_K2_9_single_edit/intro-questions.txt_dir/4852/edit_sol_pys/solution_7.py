

def dpg(str):
    if '+' not in str:
        return 1
    else:
        count = 0
        for i in range(len(str)):
            if str[i] == '+':
                count += dpg(str[:i]) * dpg(str[i+1:])
        return count

print(dpg(input()))
