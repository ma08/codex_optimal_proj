
n = int(input())
s = input()

cnt = 0

for i in "pwgy":
    if s.count(i) > 0:
        cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
