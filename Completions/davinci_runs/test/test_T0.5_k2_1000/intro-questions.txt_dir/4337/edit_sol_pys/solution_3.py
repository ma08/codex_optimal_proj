
n = int(input())
s = input()

cnt = 0

if s.count("P") >= 1:
    cnt += 1
if s.count("W") >= 1:
    cnt += 1
if s.count("G") >= 1:
    cnt += 1
if s.count("Y") >= 1:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
