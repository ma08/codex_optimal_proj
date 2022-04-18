import sys

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        command = sys.stdin.readline()
        if command[:10] == "Simon says":
            print(command[11:])

main()
