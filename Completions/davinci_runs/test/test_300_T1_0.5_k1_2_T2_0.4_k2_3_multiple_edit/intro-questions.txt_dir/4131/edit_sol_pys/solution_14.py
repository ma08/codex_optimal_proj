

import sys
import os

file_name = sys.argv[1]
file_size = os.path.getsize(file_name)

with open(file_name, 'rb') as f:
    file_content = f.read()

file_content = file_content.split(b'\n')

print(file_content)
