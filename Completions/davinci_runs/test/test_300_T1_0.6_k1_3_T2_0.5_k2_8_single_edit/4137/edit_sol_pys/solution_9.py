def get_file_name(path):
    return path.split("/")[-1]

if __name__ == "__main__":
    print(get_file_name("/home/user/file.txt"))
