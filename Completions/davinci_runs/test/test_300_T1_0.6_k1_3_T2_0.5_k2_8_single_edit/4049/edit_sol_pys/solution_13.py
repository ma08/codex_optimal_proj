#!/usr/bin/python

import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print "Folder listing for", path
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print prefix+f
        # Compute the prefix and pass to next level
        if os.path.isdir(path+"/"+f):
            print_files(path+"/"+f, prefix + "| ")

def duplicate_files(src_dir, dst_dir):
    """
    Duplicate all files (not directories) in src_dir to dst_dir.
    Do not overwrite existing files.
    """
    names = os.listdir(src_dir)
    for name in names:
        src_name = os.path.join(src_dir, name)
        dst_name = os.path.join(dst_dir, name)
        if os.path.isfile(src_name):
            if not os.path.exists(dst_name):
                open(dst_name, "w").write(open(src_name).read())
                print "Copying", src_name, "to", dst_name

def compare_files(path1, path2):
    """
    Compare all files in two directories.
    Return a list of files that differ.
    """
    files1 = get_dirlist(path1)
    files2 = get_dirlist(path2)
    only1 = []
    only2 = []
    both = []
    for name in files1:
        if name in files2:
            both.append(name)
        else:
            only1.append(name)
    for name in files2:
        if name not in files1:
            only2.append(name)
    return only1, only2, both

if __name__ == "__main__":
    print get_dirlist(".")
    print_files(".")
    duplicate_files("/tmp/foo", "/tmp/bar")
    print compare_files("/tmp/foo", "/tmp/bar")
