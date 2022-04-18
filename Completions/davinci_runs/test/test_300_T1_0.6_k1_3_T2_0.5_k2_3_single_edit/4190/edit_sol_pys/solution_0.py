

def main():
    n = int(input())  # Number of elements which make up the association table.
    q = int(input())  # Number Q of file names to be analyzed.
    a = [input().lower() for _ in range(n)]  # File extensions
    b = [input().lower() for _ in range(n)]  # MIME types
    for _ in range(q):
        fname = input()  # One file name per line.
        fname = fname.split('.')
        if len(fname) > 1:
            ext = fname[-1]
            if ext in a:
                print(b[a.index(ext)])
            else:
                print('UNKNOWN')
        else:
            print('UNKNOWN')

if __name__ == '__main__':
    main()
