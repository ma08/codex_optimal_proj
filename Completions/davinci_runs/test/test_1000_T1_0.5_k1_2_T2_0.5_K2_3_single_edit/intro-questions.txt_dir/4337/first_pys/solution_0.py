

n = int(input())
s = input()

cnt = 0

if s.count("P") > 0:
    cnt += 1
if s.count("W") > 0:
    cnt += 1
if s.count("G") > 0:
    cnt += 1
if s.count("Y") > 0:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")