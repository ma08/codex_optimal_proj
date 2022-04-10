


#%%

n = 5
s = "()))()"

#%%

def valid_bracket(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0

#%%

def generate_bracket(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    result = []
    for i in range(n):
        l = generate_bracket(i)
        r = generate_bracket(n-i-1)
        for l_bracket in l:
            for r_bracket in r:
                result.append("(" + l_bracket + ")" + r_bracket)
    return result

#%%

result = generate_bracket(n)
result = [r for r in result if s in r]
# print(result)
print(len(result))

#%%