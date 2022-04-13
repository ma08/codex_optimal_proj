

def main():
    n = int(input())
    inp = [int(x) for x in input().split()] 
    out = []
    for i in range(len(inp)):
        if i == 0 or i == 1:
            out.append(1-inp[i])
        elif i == 2 or i == 3 or i == 4:
            out.append(2-inp[i])
        elif i == 5:
            out.append(8-inp[i])
    print(*out)

main()
