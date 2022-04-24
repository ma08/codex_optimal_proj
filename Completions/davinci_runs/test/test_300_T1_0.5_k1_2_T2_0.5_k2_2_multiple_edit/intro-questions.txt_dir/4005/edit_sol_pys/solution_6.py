def file_read(fname):
    from itertools import islice
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    with open(fname, "r") as myfile:
        head = list(islice(myfile, 2))
        print(head)
file_read('abc.txt')
