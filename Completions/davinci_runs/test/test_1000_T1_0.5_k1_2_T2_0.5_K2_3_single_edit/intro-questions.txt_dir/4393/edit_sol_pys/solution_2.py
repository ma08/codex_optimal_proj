

n = int(input())  # number of test cases

t = input()  # string to be tested

s = []  # empty list

for i in range(n):
    if t[i] != t[i-1]:  # if the current character is different from previous
        s.append(t[i])

print(''.join(s))  # print the list as a string
