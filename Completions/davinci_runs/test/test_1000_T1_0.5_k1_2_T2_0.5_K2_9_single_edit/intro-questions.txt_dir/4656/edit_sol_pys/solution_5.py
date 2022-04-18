
import os


def get_file_names(directory):
    file_names = os.listdir(directory)
    print(file_names)



def main():
    directory = "./supplier-data/descriptions/"
    get_file_names(directory)


if __name__ == "__main__":
    main()
