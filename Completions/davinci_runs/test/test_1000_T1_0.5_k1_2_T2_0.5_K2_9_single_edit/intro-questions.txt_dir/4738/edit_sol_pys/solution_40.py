

def k_periodic(s):
    x = 1
    while x < len(s):
        if s[:-x] == s[x:]:
            return x
        x += 1
    return len(s) 

print(k_periodic(input()))
