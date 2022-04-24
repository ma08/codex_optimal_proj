

a, b, c = map(int, input().split()) #a = 소리, b = 인간, c = 짐승

sound = 0

while(b >= a and sound < c):
    b -= a
    sound += 1

print(sound)
