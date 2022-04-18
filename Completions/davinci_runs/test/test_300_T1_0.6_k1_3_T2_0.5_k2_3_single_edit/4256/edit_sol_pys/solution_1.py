

a, b, c = map(int, input().split())
while(b >= a and sound < c):
sound = 0

if(b >= a):
        b -= a
        sound += 1
else:
    sound = 0

print(sound)
