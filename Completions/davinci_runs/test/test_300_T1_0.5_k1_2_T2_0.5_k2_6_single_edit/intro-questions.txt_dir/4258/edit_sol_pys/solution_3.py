import os

def create_file(name, text=None):
    """
    Create a file
    """
    with open(name, 'w') as f:
        if text:
            f.write(text)

def create_folder(name):
    """
    Create a folder
    """
    try:
        os.mkdir(name)
    except:
        print("Error creating folder")

def get_list(folders_only=False):
    """
    Get list of files/folders in current directory
    """
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

def delete_file(name):
    """
    Delete a file
    """
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

def copy_file(name, new_name):
    """
    Copy a file
    """
    if os.path.isdir(name):
        try:
            os.mkdir(new_name)
        except:
            print("Error copying file")
    else:
        with open(name) as rf:
            with open(new_name, 'w') as wf:
                wf.write(rf.read())

def save_info(message):
    current_time = get_current_time()
    with open("log.txt", "a") as f:
        f.write(f"{current_time} - {message}")


def get_current_time():
    import datetime
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def main():
    create_file("text.dat", "some information\n")
    create_file("text2.dat", "some information\n")
    create_folder("new_folder")
    get_list()
    get_list(True)
    copy_file("text.dat", "text_copy.dat")
    copy_file("new_folder", "new_folder2")
    delete_file("text2.dat")
    delete_file("new_folder2")
    save_info("File created")

if __name__ == "__main__":
    main()
