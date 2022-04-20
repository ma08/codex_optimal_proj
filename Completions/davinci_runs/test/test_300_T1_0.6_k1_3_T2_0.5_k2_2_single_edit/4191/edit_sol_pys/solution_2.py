

def main(inp):
    if inp[0] == inp[2] and inp[1] == inp[3]:
        return 0
    return '1'

if __name__ == '__main__':
    inp = []
    for i in range(4):
        inp.append(int(input()))
    print(main(inp))
