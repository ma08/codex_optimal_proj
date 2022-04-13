import sys

def main():
    file_name = sys.stdin.readline().strip()
    file = open(file_name, 'r')
    print(file.read())
    file.close()

main()
