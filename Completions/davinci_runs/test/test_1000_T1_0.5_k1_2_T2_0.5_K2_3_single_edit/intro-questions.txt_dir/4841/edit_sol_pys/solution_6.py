

n = int(input()) 
s = input().split()

if len(s) != n:
    print("something is fishy")
else:
    for i in range(n):
        if s[i] == "mumble": 
            continue
        if int(s[i]) != i+1:
            print("something is fishy")
            break
    else:
        print("makes sense")
