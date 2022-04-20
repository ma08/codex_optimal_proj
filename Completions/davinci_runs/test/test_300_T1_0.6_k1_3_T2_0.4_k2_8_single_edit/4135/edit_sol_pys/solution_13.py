def reverse(n, t):
    s = ""
    for i in range(n, 0, -1):
        if n % i == 0:
            s += t[i-1::i][::-1]
            t = t[:i-1] + s[-i:] + t[i:]
    return s


n = int(input())
t = input()
print(reverse(n, t))
