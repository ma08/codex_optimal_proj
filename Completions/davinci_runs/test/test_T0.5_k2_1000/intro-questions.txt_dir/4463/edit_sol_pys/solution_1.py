
def main():
    s = input()
    t = input()
    if sorted(s) <= sorted(t, reverse=True):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
