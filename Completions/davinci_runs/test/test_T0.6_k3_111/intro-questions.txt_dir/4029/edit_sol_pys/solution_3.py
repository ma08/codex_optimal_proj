
n = input()

if int(n) % 2 == 0:
    print(0)
    quit()

if int(n[:-1]) % 2 == 0:
    print(1)
    quit()

if int(n[:-2]) % 2 == 0:
    print(2)
    quit()

if int(n[:-3]) % 2 == 0:
    print(3)
    quit()

print(-1)
