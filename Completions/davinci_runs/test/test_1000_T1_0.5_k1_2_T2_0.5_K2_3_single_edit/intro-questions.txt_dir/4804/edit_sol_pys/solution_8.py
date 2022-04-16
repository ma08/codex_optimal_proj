import os


def print_directory_content(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_content(sChildPath)
        else:
            print(sChildPath)

print_directory_content(".")
