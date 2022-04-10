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
    except FileExistsError:
        print('Folder already exist')


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


if __name__ == '__main__':
    create_file('text.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_file('text.dat')
    delete_file('new_folder')
