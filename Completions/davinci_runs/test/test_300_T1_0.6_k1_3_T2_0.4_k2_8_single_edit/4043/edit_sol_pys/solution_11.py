import os
import sys
import time
import shutil
import zipfile

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print('Usage: python3 file.py [OPTION] [PATH]')
            print('Create a new file or directory')
            print('  -h, --help       display this help and exit')
            print('  -f, --file       create a new file')
            print('  -d, --dir        create a new directory')
            print('  -z, --zip        create a new zip file')
            print('  -u, --unzip      unzip a zip file')
            print('  -r, --remove     remove a file or directory')
            print('  -c, --copy       copy a file or directory')
            print('  -m, --move       move a file or directory')
            print('  -s, --search     search a file or directory')
            print('  -l, --list       list all files and directories')
            print('  -a, --all        list all files and directories with details')
            print('  -p, --path       list the current path')
            print('  -e, --edit       edit a file')
            print('  -o, --open       open a file')
            print('  -v, --version    display version info and exit')
            print('  -i, --info       display file or directory info')
            print('  -b, --back       back to the previous directory')
            print('  -g, --goto       go to the specified directory')
            print('  -t, --tree       display directory tree')
        elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
            print('file.py version 1.0.0')
        elif sys.argv[1] == '-f' or sys.argv[1] == '--file':
            if len(sys.argv) > 2:
                with open(sys.argv[2], 'w'):
                    pass
            else:
                print('file.py: missing file operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-d' or sys.argv[1] == '--dir':
            if len(sys.argv) > 2:
                os.mkdir(sys.argv[2])
            else:
                print('file.py: missing directory operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-z' or sys.argv[1] == '--zip':
            if len(sys.argv) > 2:
                zip = zipfile.ZipFile(sys.argv[2] + '.zip', 'w', zipfile.ZIP_DEFLATED)
                zip.close()
            else:
                print('file.py: missing zip file operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-u' or sys.argv[1] == '--unzip':
            if len(sys.argv) > 2:
                zip = zipfile.ZipFile(sys.argv[2], 'r')
                zip.extractall(sys.argv[2][:-4])
                zip.close()
            else:
                print('file.py: missing zip file operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-r' or sys.argv[1] == '--remove':
            if len(sys.argv) > 2:
                if os.path.isdir(sys.argv[2]):
                    shutil.rmtree(sys.argv[2])
                else:
                    os.remove(sys.argv[2])
            else:
                print('file.py: missing file or directory operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-c' or sys.argv[1] == '--copy':
            if len(sys.argv) > 3:
                if os.path.isdir(sys.argv[2]):
                    shutil.copytree(sys.argv[2], sys.argv[3])
                else:
                    shutil.copyfile(sys.argv[2], sys.argv[3])
            else:
                print('file.py: missing file or directory operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-m' or sys.argv[1] == '--move':
            if len(sys.argv) > 3:
                if os.path.isdir(sys.argv[2]):
                    shutil.move(sys.argv[2], sys.argv[3])
                else:
                    shutil.move(sys.argv[2], sys.argv[3])
            else:
                print('file.py: missing file or directory operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-s' or sys.argv[1] == '--search':
            if len(sys.argv) > 2:
                for root, dirs, files in os.walk(os.getcwd()):
                    if sys.argv[2] in dirs or sys.argv[2] in files:
                        print(os.path.join(root, sys.argv[2]))
            else:
                print('file.py: missing file or directory operand')
                print('Try \'file.py --help\' for more information.')
        elif sys.argv[1] == '-l' or sys.argv[1] == '--list':
            if len(sys.argv) > 2:
                for file in os.listdir(sys.argv[2]):
                    print(file)
            else:
                for file in os.listdir(os.getcwd()):
                    print(file)
        elif sys.argv[1] == '-a' or sys.argv[1] == '--all':
            if len(sys.argv) > 2:
                for file in os.listdir(sys.argv[2]):
                    info = os.stat(sys.argv[2] + '/' + file)
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info.st_mtime)), end=' ')
                    if os.path.isdir(sys.argv[2] + '/' + file):
                        print('<DIR>', end=' ')
                    else:
                        print(info.st_size, end=' ')
                    print(file)
            else:
                for file in os.listdir(os.getcwd()):
                    info = os.stat(file)
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info.st_mtime)), end=' ')
                    if os.path.isdir(file):
                        print('<DIR>', end=' ')
                    else:
                        print(info.st_size, end=' ')
                    print(file)
        elif sys.argv[1] == '-p' or sys.argv[1] == '--path':
            print(os.getcwd())
        elif sys.argv[1] == '-e' or sys.argv[1] == '--edit':
            if len(sys.argv) > 2:
