

def main():
    num = input()
    print('Yes' if len(num) == 1 or sorted(num) == list(num) else 'No')

main()
