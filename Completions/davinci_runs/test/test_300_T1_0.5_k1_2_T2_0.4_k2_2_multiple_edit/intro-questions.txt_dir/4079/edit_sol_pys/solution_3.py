
n = int(input())
for i in range(n):
    i = input()
    if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1:
        print("Yes")
    else:
        print("No")
