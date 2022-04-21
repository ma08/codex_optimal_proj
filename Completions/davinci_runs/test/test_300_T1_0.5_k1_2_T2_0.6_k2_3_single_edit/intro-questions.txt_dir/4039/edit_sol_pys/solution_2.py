
    file = open("file.txt","w+")
    for i in range(10):
        file.write("This is line %d\r\n" % (i+1))
    file.close()
def main():
    pass

if __name__ == "__main__":
    main()
