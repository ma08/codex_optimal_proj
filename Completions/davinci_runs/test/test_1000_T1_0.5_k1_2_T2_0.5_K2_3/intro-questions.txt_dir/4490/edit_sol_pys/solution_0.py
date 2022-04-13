

def main():
    s = input()
    print(s[::-1].replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper())

if __name__ == '__main__':
    main()
