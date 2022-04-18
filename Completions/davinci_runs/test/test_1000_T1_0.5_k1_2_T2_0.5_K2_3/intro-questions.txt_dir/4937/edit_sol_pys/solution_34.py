

def main():
    s = input()
    t = input()
    print('Yes' if s == t or s == t[::-1] else 'No')

main()
