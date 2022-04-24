
S = str(input())

def rotate(s):
    return s[-1] + s[:-1]
T = str(input())

if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    S = rotate(S)
    if S == T:
        print("Yes")
        exit()
print("No")
