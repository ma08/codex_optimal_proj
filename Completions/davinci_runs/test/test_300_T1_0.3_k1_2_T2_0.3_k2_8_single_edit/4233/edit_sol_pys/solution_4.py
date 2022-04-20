

def main(file):
    with open(file, 'r') as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    main('file.py')
