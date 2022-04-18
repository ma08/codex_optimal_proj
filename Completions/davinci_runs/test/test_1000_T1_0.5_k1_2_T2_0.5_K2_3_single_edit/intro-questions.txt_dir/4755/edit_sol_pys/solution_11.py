

# put your python code here
s = input()
s = s.replace("h", "")
s = s.replace("e", "")
s = s.replace("l", "")
s = s.replace("o", "")
s = s.replace("w", "")
s = s.replace("r", "")
s = s.replace("d", "")
if len(s) == 0:
    print("YES")
else:
    print("NO")
