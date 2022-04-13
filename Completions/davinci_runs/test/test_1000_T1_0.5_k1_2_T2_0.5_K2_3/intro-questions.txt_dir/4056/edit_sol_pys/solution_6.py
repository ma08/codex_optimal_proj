'''
Created on May 18, 2016

@author: javi
'''

import os
import re
import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print ("Usage: python file.py <file>")
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print ("Error: File '%s' not found" % filename)
        sys.exit(1)
    f = open(filename)
    file_contents = f.read()
    f.close()
    if not file_contents:
        print ("Error: File '%s' is empty" % filename)
        sys.exit(1)
    file_type = subprocess.check_output(["file", filename]).decode("utf-8")
    file_type = re.search(r":\s*(.*)\s*$", file_type).group(1)
    print ("%s: %s" % (filename, file_type))


if __name__ == "__main__":
    main()
