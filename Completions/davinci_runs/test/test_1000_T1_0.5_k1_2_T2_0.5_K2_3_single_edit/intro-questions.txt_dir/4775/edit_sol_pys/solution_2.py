
a,b = input().split()  # input the two strings

for i in range(len(b)):  # find the first index of the common character
    if b[i] in a:        # in both the strings
        j = 0
        while j < len(a):
            if a[j] == b[i]:
                break
            j+=1
        break

for i in range(len(b)):
    if b[i] in a:
        print("."*j + b[i] + "."*(len(a)-j-1))
    else:
        print("."*len(a))
