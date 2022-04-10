

def main():
    a, b, x = map(int, input().split())
    s = ''
    for i in range(a):
        s += '0'
    for i in range(b):
        s += '1'
    for i in range(x):
        if i % 2 == 0:
            s = s[:i+1] + s[i+1].replace('0', '1') + s[i+2:]
        else:
            s = s[:i+1] + s[i+1].replace('1', '0') + s[i+2:]
    print(s)

main()
