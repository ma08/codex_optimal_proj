import sys

def main():
    name = sys.stdin.readline().strip()
    compact = name[0] # compact is a string
    for i in range(1, len(name)):
        if name[i] != compact[-1]: # compact[-1] is the last element of compact
            compact += name[i]
    print(compact)

main()
