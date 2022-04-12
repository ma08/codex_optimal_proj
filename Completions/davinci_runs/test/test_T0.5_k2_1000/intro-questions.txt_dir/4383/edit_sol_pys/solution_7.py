
y = int(input())
x = int(input())

if x in [3, 5, 7, 11]:
    print("YES") if y % x == 0 else print("NO")
else:
    print("NO")
