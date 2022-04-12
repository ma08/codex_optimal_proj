s = input()
res = ""
for char in s:
    if char == "0":
        res += "0"
    elif char == "1":
        res += "1"
    else:
        res = res[:-1]

print(res)
