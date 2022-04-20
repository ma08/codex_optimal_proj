

a, b, c = map(int, input().split())

sound = 0

if(b >= a):
    while(b >= a and sound < c):
        b -= a
        if(sound == c):
            break
        sound += 1
else:
    sound = 0

print(sound)
