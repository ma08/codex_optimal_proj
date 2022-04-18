
n = int(input())
s = input()

cnt = 0

if "p" in s:
    cnt += 1
if "w" in s:
    cnt += 1
if "g" in s:
    cnt += 1
if "y" in s:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
