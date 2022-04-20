import os


def main():

    f = open('file.txt', 'r')
    print(f.read())
    f.close()

    f = open('file.txt', 'a')
    f.write('\nHello, world!')
    f.close()

    f = open('file.txt', 'r')
    print(f.read())
    f.close()

    os.remove('file.txt')



if __name__ == '__main__':
    main()
