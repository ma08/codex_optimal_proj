
with open("file.txt", "r") as f:
    s = f.read()
    for i in range(len(s)):
        s = s[:i] + "x" + s[i+1:]
    print(s)
