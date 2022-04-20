

#!/usr/bin/python3

import sys
import os
import subprocess

#print(sys.argv[1])

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]

def get_file_name(file_name):
    return os.path.splitext(file_name)[0]

def check_file_extension(file_name):
    if get_file_extension(file_name) == ".mp3":
        return True
    else:
        return False

def convert_mp3_to_wav(file_name):
    command = "ffmpeg -i " + file_name + " " + get_file_name(file_name) + ".wav"
    subprocess.call(command, shell=True)

def convert_wav_to_mp3(file_name):
    command = "ffmpeg -i " + file_name + " " + get_file_name(file_name) + ".mp3"
    subprocess.call(command, shell=True)

def convert_file(file_name):
    if check_file_extension(file_name):
        convert_mp3_to_wav(file_name)
    else:
        convert_wav_to_mp3(file_name)

def check_argument(arg):
    if arg == "convert":
        convert_file(sys.argv[2])
    else:
        print("Error: wrong argument")


def main():
    check_argument(sys.argv[1])

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print("Error: wrong number of arguments")
