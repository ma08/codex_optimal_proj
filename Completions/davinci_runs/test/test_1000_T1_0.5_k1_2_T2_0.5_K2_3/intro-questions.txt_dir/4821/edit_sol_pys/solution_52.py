

def main():
    n = int(input())
    d = {}
    for i in range(n):
        line = input().split()
        d[line[0]] = line[1]
    while True:
        try:
            name = input()
            if name in d:
                print(name, "=", d[name], sep="")
            else:
                print("Not found")
        except:
            break

main()
