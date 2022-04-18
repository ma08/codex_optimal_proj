

n = int(input())
s = input()
s = ""
for i in range(n, 0, -1): 
    if n % i == 0:
        t += s[i-1::i][::-1]
        s = s[:i-1] + t[-i:] + s[i:]
print(t)
