

s = input()

if len(s) < 4 or len(s) > 10:
    print("WA")
    exit()

if s[0] != "A":
    print("WA")
    exit()

c_count = 0

for i in range(2, len(s) - 1):
    if s[i] == "C":
        c_count += 1
    elif s[i].islower() == False:
        print("WA")
        exit()

if c_count != 1:
    print("WA")
    exit()

if s[-1].islower() == False:
    print("WA")
    exit()

print("AC")