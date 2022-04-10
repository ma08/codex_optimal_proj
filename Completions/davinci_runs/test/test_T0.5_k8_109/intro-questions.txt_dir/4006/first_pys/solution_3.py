

def func(n):
    if n%10!=0:
        return n+1
    else:
        return func(n//10)

def main(n):
    s=set()
    s.add(n)
    while True:
        n=func(n)
        if n in s:
            break
        else:
            s.add(n)
    return len(s)

n=int(input())
print(main(n))