import os

import re
import shutil
import subprocess
import tempfile
import time
import zipfile
import sys

def main():
    if len(sys.argv) == 2:
        zip_file = sys.argv[1]
        print(solve(zip_file))
    else:
        print('Please specify zip file')

def solve(zip_file):
    temp_dir = tempfile.mkdtemp()
    try:
        z = zipfile.ZipFile(zip_file)
        z.extractall(temp_dir)
        z.close()

        for filename in os.listdir(temp_dir):
            if not filename.endswith('.py'):
                continue
            filepath = os.path.join(temp_dir, filename)
            if not check_syntax(filepath):
                return False
        return True
    finally:
        shutil.rmtree(temp_dir)

def check_syntax(filepath):
    with open(filepath) as f:
        source = f.read()
    try:
        compile(source, filepath, 'exec')
    except SyntaxError:
        return False
    return True

if __name__ == '__main__':
    main()
