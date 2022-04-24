



s = input()
t = input()


removed = 0


left = 0
right = 0


while right < len(s):
   
    if s[right] in t:
        left = right
   
    else:
        removed += 1
    
    right += 1


print(removed)
