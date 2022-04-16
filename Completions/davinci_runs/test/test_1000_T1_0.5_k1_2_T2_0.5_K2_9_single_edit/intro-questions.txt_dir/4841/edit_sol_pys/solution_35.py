

n = int(input())
s = input().split()

if len(s) != n:
    print("SOMETHING IS FISHY")
else:
    for i in range(n):
        if s[i] == "mumble":
            continue
        if int(s[i]) != i+1:
            print("SOMETHING IS FISHY")
            break
    else:
        print("MAKES SENSE")
