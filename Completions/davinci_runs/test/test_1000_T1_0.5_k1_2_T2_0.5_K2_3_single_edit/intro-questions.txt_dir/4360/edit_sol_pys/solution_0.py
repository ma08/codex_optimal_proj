

import os
import sys

file_name = sys.argv[1]
str = sys.argv[2]

with open(file_name, "r") as file:
    for line in file:
        if str in line:
            print(line)

#os.system("cat {0} | grep {1}".format(file_name, str))
