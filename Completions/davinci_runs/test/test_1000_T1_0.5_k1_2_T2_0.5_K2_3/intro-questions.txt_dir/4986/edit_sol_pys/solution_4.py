import sys
import os
from os.path import join, dirname, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from lib.file import File


file = File("../data/hightemp.txt")

for i in range(len(s)):
    if s[i] != t[i]:
        result += s[i]

print(result)
