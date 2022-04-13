

s = input()  # input 1st string
t = input()  # input 2nd string

if len(s) < len(t):  # if 1st string is shorter than 2nd string
    print("Yes")
elif len(s) > len(t):  # if s is longer than t
    print("No")
else:  # if s and t are equal
    for i in range(len(s)):  # iterate through the string
        if s[i] < t[i]:  # if s is smaller than t
            print("Yes")
            break
        elif s[i] > t[i]:
            print("No")
            break
        else:
            if i == len(s) - 1:
                print("No")
