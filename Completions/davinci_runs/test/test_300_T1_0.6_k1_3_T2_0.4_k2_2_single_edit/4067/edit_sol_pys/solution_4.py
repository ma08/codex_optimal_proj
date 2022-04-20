

def main():
    n = int(input())
    s = input()

    s = swap(s, '012', '120')
    s = swap(s, '102', '210')
    s = swap(s, '201', '012')

    print(s)

def swap(s, a, b):
    i = 0
    while i < len(s):
        if s[i:i+3] == a:
            s = s[:i] + b + s[i+3:]
        i = i + 1
    return s

main()
