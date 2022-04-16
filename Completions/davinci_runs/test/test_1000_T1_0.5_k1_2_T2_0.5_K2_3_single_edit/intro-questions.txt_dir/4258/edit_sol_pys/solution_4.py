import os
import sys
import getpass

user = getpass.getuser()

def create_file(name, text=''):
    with open(name, 'w') as f:
        f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Folder exists")

def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print("File doesn't exist")

def copy_file(name, new_name):
    try:
        with open(name, 'r') as rf:
            with open(new_name, 'w') as wf:
                for line in rf:
                    wf.write(line)
    except FileNotFoundError:
        print("File doesn't exist")

def save_info(message):
    current_directory = os.getcwd()
    os.chdir(f'/home/{user}/Documents')
    with open('log.txt', 'a') as f:
        f.write(message)
    os.chdir(current_directory)

def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        return

    command = sys.argv[1]
    if command == 'list':
        print(os.listdir())
    elif command == 'create_file':
        create_file(sys.argv[2])
        save_info(f"{user} created {sys.argv[2]}\n")
    elif command == 'create_folder':
        create_folder(sys.argv[2])
        save_info(f"{user} created {sys.argv[2]}\n")
    elif command == 'delete':
        delete_file(sys.argv[2])
        save_info(f"{user} deleted {sys.argv[2]}\n")
    elif command == 'copy':
        copy_file(sys.argv[2], sys.argv[3])
        save_info(f"{user} copied {sys.argv[2]} to {sys.argv[3]}\n")
    elif command == 'help':
        print("""
        list - lists all files and folders in current directory
        create_file - creates a file
        create_folder - creates a folder
        delete - deletes a file
        copy - copies a file to another file
        """)
    else:
        print("Unknown command")

if __name__ == '__main__':
    main()
