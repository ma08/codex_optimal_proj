import sys

def main():
    name = sys.stdin.readline().strip()
    compact_name = name[0]
    for i in range(1, len(name)):
        if name[i] != compact_name[-1]:
            compact_name += name[i]
    print(compact_name)

main()
