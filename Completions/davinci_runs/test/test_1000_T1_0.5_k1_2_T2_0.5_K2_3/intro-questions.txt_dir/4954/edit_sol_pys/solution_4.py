

def main():
    # get the input from the user
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    # create a new file to write to
    file = open("output.txt", "w")

    for line in lines:
        file.write(line)

    file.close()

if __name__ == "__main__":
    main()
