

n = int(input())

for i in range(n):
    s = input()
    if len(s)==1:
        print("Yes")
    else:
        for j in range(len(s)-1):
            if ord(s[j])+1!=ord(s[j+1]) and ord(s[j])-1!=ord(s[j+1]):
                print("No")
                break
            elif j==len(s)-2:
                print("Yes")