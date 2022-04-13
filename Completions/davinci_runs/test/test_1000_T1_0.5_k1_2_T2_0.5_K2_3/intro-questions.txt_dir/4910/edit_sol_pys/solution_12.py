import os

path = "python-challenge/file"
os.chdir(path)
os.system("ls -l")

with open("data.txt", "r") as f:
    for line in f:
        print(line)

with open("data.txt", "w") as f:
    f.write("hello world")
