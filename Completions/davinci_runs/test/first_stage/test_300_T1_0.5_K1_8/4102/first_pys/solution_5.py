

#-----Solution-----

def isLucky(n):
    s = str(n)
    l = len(s)
    half = l // 2
    first_half = s[:half]
    second_half = s[half:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

print("Yes" if isLucky(int(input())) else "No")