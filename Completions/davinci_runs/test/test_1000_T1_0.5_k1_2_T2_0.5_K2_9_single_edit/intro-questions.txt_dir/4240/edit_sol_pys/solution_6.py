
s = input()
t = input()

if s == t:
    print("Yes")
else:
    if len(s) == len(t):
        for i in range(len(s)):
            if s == t: # sとtが一致したら終了
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1] # sの先頭を末尾に移動させる
        else:
            print("No")
    else:
        print("No")
