import os
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '-a':
            print(os.getcwd())
        elif sys.argv[1] == '-b':
            print(os.listdir())
        elif sys.argv[1] == '-c':
            print(os.getpid())
        elif sys.argv[1] == '-d':
            print(os.getppid())
        elif sys.argv[1] == '-e':
            print(os.getlogin())
        elif sys.argv[1] == '-f':
            print(os.getuid())
        elif sys.argv[1] == '-g':
            print(os.getgid())
        elif sys.argv[1] == '-h':
            print(os.getegid())
        elif sys.argv[1] == '-i':
            print(os.geteuid())
        elif sys.argv[1] == '-j':
            print(os.getgroups())
        elif sys.argv[1] == '-k':
            print(os.getloadavg())
        elif sys.argv[1] == '-l':
            print(os.getenv())
        elif sys.argv[1] == '-m':
            print(os.getenv('PATH'))
        elif sys.argv[1] == '-n':
            print(os.getenv('PWD'))
        elif sys.argv[1] == '-o':
            print(time.time())
        elif sys.argv[1] == '-p':
            print(time.localtime())
        elif sys.argv[1] == '-q':
            print(time.asctime())
        elif sys.argv[1] == '-r':
            print(time.ctime())
        elif sys.argv[1] == '-s':
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
        elif sys.argv[1] == '-t':
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        elif sys.argv[1] == '-u':
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        elif sys.argv[1] == '-v':
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        elif sys.argv[1] == '-w':
            print(os.uname())
        elif sys.argv[1] == '-x':
            print(os.getcwd())
        elif sys.argv[1] == '-y':
            print(os.getcwd())
        elif sys.argv[1] == '-z':
            print(os.getcwd())
        else:
            print("Invalid flag")
    else:
        print("No flag")
