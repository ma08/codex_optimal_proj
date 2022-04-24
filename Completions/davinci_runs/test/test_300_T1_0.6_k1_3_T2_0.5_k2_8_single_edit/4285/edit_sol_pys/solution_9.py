

def main():
    n = int(input())
    s = input()
    a = 0
    b = 0
    c = 0
    count = 1
    for i in range(n):
        if s[i] == "a":
            a += 1
        elif s[i] == "b":
            b += 1
        elif s[i] == "c":
            c += 1
        else:
            count = (count * 3) % 1000000007
    print (a * b * c * count) % 1000000007

main()
