
n = int(input())
s = input()

cnt = 0

if "P" in s:
    cnt += 1
if "W" in s:
    cnt += 1
if "G" in s:
    cnt += 1
if "Y" in s:
    cnt += 1

if cnt == 3:
    print("Three")
else:
    print("Four")
