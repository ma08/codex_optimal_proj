n = input()

if int(n) % 25 == 0 and len(n) != 1:
    print(0)
    quit()

if int(n[:-1]) % 25 == 0 and len(n) != 2:
    print(1)
    quit()

if int(n[:-2]) % 25 == 0 and len(n) != 3:
    print(2)
    quit()

if int(n[:-3]) % 25 == 0 and len(n) != 4:
    print(3)
    quit()

print(-1)
