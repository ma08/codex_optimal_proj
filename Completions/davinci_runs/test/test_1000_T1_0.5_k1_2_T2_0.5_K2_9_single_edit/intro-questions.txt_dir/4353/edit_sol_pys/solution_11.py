

#s = input()
#print(s.replace(",", " "))

def main():
    # get the file name
    fname = input('Enter the file name: ')

    # attempt to open the file for reading
    try:
        f = open(fname, 'r')
    except IOError:
        print('File not found!')
        return

    # display the file contents
    for line in f:
        print(line.rstrip('\n'))

    # close the file
    f.close()


# call the main function
main()
