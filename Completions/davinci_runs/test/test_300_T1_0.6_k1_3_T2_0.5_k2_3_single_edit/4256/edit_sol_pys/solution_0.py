

a, b, c = map(int, input())

sound = 0

if(b >= a):
    while(b >= a and sound < c):
        b -= a
        sound += 1
else:
    sound = 0

print(sound)
