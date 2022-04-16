

def main():
    f = open("file.txt", "r")
    s = f.read()
    f.close()
    print(s)

if __name__ == "__main__":
    main()
