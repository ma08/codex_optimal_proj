

n = int(input())  # enter the number of characters
t = input()  # enter the string
s = ""
for i in range(n, 0, -1):  # check if the number is divisible by the string
    if n % i == 0:
        s += t[i-1::i][::-1]  # reverse the string
        t = t[:i-1] + s[-i:] + t[i:]  # concatenate the string
print(s)
