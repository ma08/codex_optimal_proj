import sys

def main():
    filename = sys.stdin.readline().strip()
    compact = filename[0] # first character
    for i in range(1, len(filename)): # skip first character
        if filename[i] != compact[-1]:
            compact += filename[i]
    print(compact)

main()
