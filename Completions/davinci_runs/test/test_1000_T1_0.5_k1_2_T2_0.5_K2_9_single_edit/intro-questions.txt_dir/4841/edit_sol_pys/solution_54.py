

n = int(input())
words = input().split()
if words[0] == "mumble":
    print("makes sense")
elif int(words[0]) != 1:
    print("something is fishy")
else:    
    for i in range(n):
        if words[i] == "mumble":
            continue
        if int(words[i]) != i + 1:
            print("something is fishy")
            break
    else:
        print("makes sense")
