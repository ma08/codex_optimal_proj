

def main(inp):
    if inp[0] == inp[2] or inp[1] == inp[3]:
        return 0
    elif abs(inp[0] - inp[2]) == abs(inp[1] - inp[3]):
        return 1
    else:
        return 2

if __name__ == '__main__':
    inp = []
    for i in range(4):
        inp.append(int(input()))
    print(main(inp))
