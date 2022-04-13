

s = input()  # input string s
t = input()  # input string t

if len(s) < len(t):  # if s is shorter than t
    print("Yes")
elif len(s) > len(t):  # if s is longer than t
    print("No")
else:  # if s and t are equal
    for i in range(len(s)):  # iterate through the string
        if s[i] < t[i]:  # if s is smaller than t
            print("Yes")
            break
        elif s[i] > t[i]:  # if s is bigger than t
            print("No")
            break
        else:  # if s and t are equal
            if i == len(s) - 1:  # if iterating through s is finished
                print("No")
