
import os

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def get_py(path):
    return (file for file in get_files(path) if file.endswith(".py"))

c = Counter(s[i:i+2] for i in range(n-1))

print(max(c, key=c.get))
