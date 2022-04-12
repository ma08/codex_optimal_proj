n = int(input())
a = list(map(int, input().split()))


a.sort(reverse=True)

cnt = 0

if s.count("p") > 0:
    cnt += 1
if s.count("w") > 0:
    cnt += 1
if s.count("G") > 0:
    cnt += 1
if s.count("Y") > 0:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
