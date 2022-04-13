

def main():
    name = input() #needs a file name
    print(name[0] + "".join([x[0] for x in name.split("-")[1:]]))  #prints the first letter of each word in the file name

if __name__ == "__main__":
    main()
