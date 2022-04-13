
import sys

def main():
    s = sys.stdin.read()
    if s.find('ss') != -1:
        print("hiss")
    else: 
        print("no hiss")

main()
