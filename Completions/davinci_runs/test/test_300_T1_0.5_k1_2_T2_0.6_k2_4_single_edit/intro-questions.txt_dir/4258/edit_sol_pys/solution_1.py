import os
import sys
import stat
 
def main():
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        os.chmod(file_name, stat.S_IWRITE)
        os.remove(file_name)
        print("File " + file_name + " deleted")
    else:
        print("File " + file_name + " not found")
 
if __name__ == '__main__':
    main()
