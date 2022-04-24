

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    string = input()
    print(bool(re.search(r'^[+-]?\d*?\.{1}\d+$', string)))
