import os
import sys
import shutil
import pytest

def test_file_exists():
    assert os.path.isfile("/home/student-00-c7d9b9f3e1f4/test_file.txt")

def test_file_contents():
    f = open("/home/student-00-c7d9b9f3e1f4/test_file.txt","r")
    contents = f.read()
    assert contents == "This is a test file\n"

def test_file_permissions():
    assert oct(os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt").st_mode & 0o777) == "0666"

def test_file_owner():
    assert os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt").st_uid == 0

def test_file_group():
    assert os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt").st_gid == 0

def test_file_type():
    assert os.path.isfile("/home/student-00-c7d9b9f3e1f4/test_file.txt")

def test_file_size():
    assert os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt").st_size == 24

def test_file_readonly():
    os.chmod("/home/student-00-c7d9b9f3e1f4/test_file.txt", 0o444)
    assert oct(os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt").st_mode & 0o777) == "0444"
    os.chmod("/home/student-00-c7d9b9f3e1f4/test_file.txt", 0o666)

def test_file_delete():
    os.remove("/home/student-00-c7d9b9f3e1f4/test_file.txt")
    with pytest.raises(OSError):
        os.stat("/home/student-00-c7d9b9f3e1f4/test_file.txt")
    f = open("/home/student-00-c7d9b9f3e1f4/test_file.txt","w+")
    f.write("This is a test file\n")
    f.close()
