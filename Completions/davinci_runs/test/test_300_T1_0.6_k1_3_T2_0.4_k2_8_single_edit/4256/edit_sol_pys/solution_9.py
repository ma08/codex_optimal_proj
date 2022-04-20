

a, b, c = map(int, input().split()) # get input

sound = 0

if(b >= a): # if b is greater than or equal to a
    while(b >= a and sound < c):
        b -= a
        sound += 1
else:
    sound = 0

print(sound)
