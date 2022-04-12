
n = int(input("n: "))

minutes = 0
seconds = 0

for i in range(n):
    m, s = map(int, input("m, s: ").split())
    minutes += m
    seconds += s

if seconds/minutes > 60:
    print("measurement error")
else:
    print(seconds/minutes)
