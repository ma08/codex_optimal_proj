
s = input()  # type: str
result = ""  # type: str
for char in s:  # type: str
    if char == "0":  # type: str
        result += "0"  # type: str
    elif char == "1":  # type: str
        result += "1"  # type: str
    else:  # type: str
        result = result[:-1]  # type: str
print(result)  # type: str
