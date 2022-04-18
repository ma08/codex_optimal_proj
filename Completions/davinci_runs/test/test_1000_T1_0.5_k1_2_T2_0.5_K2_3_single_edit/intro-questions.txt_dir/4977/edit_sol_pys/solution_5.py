

def main():
    a, b = map(int, input('Enter two numbers: ').split())
    c, d = map(int, input('Enter two numbers: ').split())
    t = int(input('Enter a number: '))

    if (a - c) ** 2 + (b - d) ** 2 == t ** 2:
        print('Y')
    else:
        print('N')

main()
