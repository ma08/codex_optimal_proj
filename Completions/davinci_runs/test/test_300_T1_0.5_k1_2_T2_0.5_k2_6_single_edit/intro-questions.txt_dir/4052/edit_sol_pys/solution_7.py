#!/usr/bin/python

import os
import sys
import time

#def main():
#    print "Hello World"


#if __name__ == "__main__":
#    main()

def file_create(filename):
    f = open(filename, "w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()

def file_read(filename):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)
    f.close()

def file_append(filename):
    f = open(filename, "a")
    for i in range(2):
        f.write("Appended line %d\r\n" % (i+1))
    f.close()
    
def file_delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

def file_rename(filename1, filename2):
    os.rename(filename1, filename2)

def file_create_dir(dirname):
    os.mkdir(dirname)

def file_remove_dir(dirname):
    os.rmdir(dirname)

def file_rename_dir(dirname1, dirname2):
    os.rename(dirname1, dirname2)

def file_exist(filename):
    if os.path.exists(filename):
        print("File exists")
    else:
        print("File does not exist")

def file_stats(filename):
    st = os.stat(filename)
    print("File stats:")
    print("    Size: %d" % st.st_size)
    print("    Permissions: %d" % st.st_mode)
    print("    Owner: %d" % st.st_uid)
    print("    Device: %d" % st.st_dev)
    print("    Created: %s" % time.ctime(st.st_ctime))
    print("    Last modified: %s" % time.ctime(st.st_mtime))
    print("    Last accessed: %s" % time.ctime(st.st_atime))

def file_walk(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def file_list_dir(dirname):
    for name in os.listdir(dirname):
        print(name)

def file_list_dir_full(dirname):
    for name in os.listdir(dirname):
        print(os.path.join(dirname, name))

def file_list_dir_recursive(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print(os.path.join(root, name))

def file_list_dir_recursive_full(dirname):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def file_get_current_dir():
    print(os.getcwd())

def file_change_dir(dirname):
    os.chdir(dirname)

def file_get_env(env):
    print(os.getenv(env))

def file_set_env(env, val):
    os.putenv(env, val)

def file_unset_env(env):
    os.unsetenv(env)

def file_get_pid():
    print(os.getpid())

def file_get_login():
    print(os.getlogin())

def file_get_uid():
    print(os.getuid())

def file_get_gid():
    print(os.getgid())

def file_get_groups():
    print(os.getgroups())

def file_get_hostname():
    print(os.uname())

def file_get_environ():
    print(os.environ)

def file_get_environ_item(item):
    print(os.environ.get(item))











































































































































































































































































































































































































