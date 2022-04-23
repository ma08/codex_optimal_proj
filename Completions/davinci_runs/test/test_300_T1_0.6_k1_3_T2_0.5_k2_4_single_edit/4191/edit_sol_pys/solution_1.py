

def main(inp: list):
    if inp[0] == inp[2] or inp[1] == inp[3]:
        return 0
    return 1

if __name__ == '__main__':
    inp = []
    for _ in range(4):
        inp.append(int(input()))
    print(main(inp))
