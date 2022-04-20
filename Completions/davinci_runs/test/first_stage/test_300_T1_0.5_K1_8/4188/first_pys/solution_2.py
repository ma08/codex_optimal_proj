
def main():
    n = int(raw_input())
    if n in [1, 5, 9, 10, 11, 16]:
        print 1
    elif n in [2, 6, 7, 8, 12, 13, 14, 15]:
        print 0
    else:
        print 2

if __name__ == '__main__':
    main()