

n = input()

if int(n) % 25 == 0:
    print(0)
    quit()

if int(n[:-1]) % 25 == 0:
    print(1)
    quit()

if int(n[:-2]) % 25 == 0:
    print(2)
    quit()

if int(n[:-3]) % 25 == 0:
    print(3)
    quit()

print(-1)