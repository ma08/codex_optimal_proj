

a, b, c = map(int, input().split()) # input

sound = 0 # variable sound

if(b >= a): # if b greater than or equal to a
    while(b >= a and sound < c): # while b greater than or equal to a and sound less than c
        b -= a # b = b - a
        sound += 1 # sound = sound + 1
else:
    sound = 0

print(sound)
