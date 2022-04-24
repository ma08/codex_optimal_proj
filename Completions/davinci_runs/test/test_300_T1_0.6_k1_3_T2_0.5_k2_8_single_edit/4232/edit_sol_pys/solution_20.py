import os
import sys
import re

def main():
    path = sys.argv[1]
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            f = open(file_path, 'r')
            content = f.read()
            f.close()

            f = open(file_path, 'w')
            content = re.sub(r'\s*(<\/?(?:html|body|img|table|tr|td|a|br|p|span|ul|li|div|meta|link|title)>)\s*', r'\1', content)
            content = re.sub(r'\s+', ' ', content)
            f.write(content)
            f.close()

if __name__ == '__main__':
    main()
