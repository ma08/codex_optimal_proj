
def main():
    s = input()
    if s[-1] == 'y':
        print(s[:-1] + 'e'*len(s))
    else:
        print(s)

if __name__ == '__main__':
    main()
