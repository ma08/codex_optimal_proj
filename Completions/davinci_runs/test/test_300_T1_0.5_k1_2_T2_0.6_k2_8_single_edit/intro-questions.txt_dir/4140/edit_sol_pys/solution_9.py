
S = input()
S = S.replace("0", "x")
S = S.replace("1", "0")
S = S.replace("x", "1")
print(S.count("1"))
