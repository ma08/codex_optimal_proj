
n = int(input())
s = input()

cnt = 0

if s.count("p") > 0:
    cnt += 1 
if s.count("w") > 0:
    cnt += 1
if s.count("g") > 0:
    cnt += 1
if s.count("y") > 0:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
