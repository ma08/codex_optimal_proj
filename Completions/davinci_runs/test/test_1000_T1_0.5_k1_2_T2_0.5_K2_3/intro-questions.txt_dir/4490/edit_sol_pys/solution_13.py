

def main():
    s = input()
    print(s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1])

if __name__ == '__main__':
    main()
