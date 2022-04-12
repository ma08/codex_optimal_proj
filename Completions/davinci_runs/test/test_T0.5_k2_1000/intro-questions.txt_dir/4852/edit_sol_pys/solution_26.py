

def dpg(string): #dpg stands for dynamic programming
    if '+' not in string and '-' not in string:
        return 1
    else:
        count = 0
        for i in range(len(string)):
            if string[i] == '+' or string[i] == '-':
                count += dpg(string[:i]) * dpg(string[i+1:])
        return count

print(dpg(input()))
