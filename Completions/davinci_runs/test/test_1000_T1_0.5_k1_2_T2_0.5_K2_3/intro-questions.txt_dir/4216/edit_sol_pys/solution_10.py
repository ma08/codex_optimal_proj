

import os

import sys

#
# Complete the timeConversion function below.


#
def timeConversion(s):
    #
    # Write your code here.
    #
    return 1



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], "w")

    s = input()

    result = timeConversion(s, 0)

    f.write(result + "\n")

    f.close()
