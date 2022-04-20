

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for i in range(2*n-2):
        s = input()
        if s in prefixes:
            suffixes.append(s)
        else:
            prefixes.append(s)
    prefixes.sort(key=len)
    suffixes.sort(key=len)
    print(''.join(['P' if i in prefixes else 'S' for i in prefixes+suffixes]))

main()