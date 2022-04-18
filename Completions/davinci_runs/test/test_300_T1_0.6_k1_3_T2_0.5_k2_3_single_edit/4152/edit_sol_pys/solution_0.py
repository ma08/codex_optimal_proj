import os

def main():
    # print the name of the OS
    print(os.name)

    # check for item existence and type
    print("Item exists: " + str(os.path.exists("textfile.txt")))
    print("Item is a file: " + str(os.path.isfile("textfile.txt")))
    print("Item is a directory: " + str(os.path.isdir("textfile.txt")))

    # work with file paths
    print("Item path: " + str(os.path.realpath("textfile.txt")))
    print("Item path and name: " + str(os.path.split(os.path.realpath("textfile.txt"))))

    # get the modification time
    t = time.ctime(os.path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt")))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
